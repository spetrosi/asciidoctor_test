#!/usr/bin/env python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: asciidoctor_wrapper

short_description: Build HTML file from AsciiDoc files.

version_added: "1.0.0"

description: This module uses the asciidoctor CLI tool to build AsciiDoc files into an HTML file.

options:
    directory:
        description: Defines the directory from where the asciidoctor must run.
        required: true
        type: str
    source_file:
        description: Defines the AsciiDoc file that you want to use for the build.
        required: true
        type: str
    output_file:
        description:
            - >-
              Defines the file where the HTML build is stored.
              The module creates the output file in the directory where the source file is stored.
        required: true
        type: str
    force:
        description: If true, recreates the HTML file even if it exists.
        required: false
        type: bool
        default: false
author:
    - Sergei Petrosian (@spetrosi)
'''

EXAMPLES = r'''
# Build the AsciiDoc book in the `/home/username/Documents/guide` directory to the guide.html file.
# The resulting build is stored in the /home/username/Documents/guide/guide.html directory
- name: Build HTML from a book in `/home/username/Documents/guide`
  asciidoctor_wrapper:
    directory: "/home/username/Documents/guide"
    source_file: master.adoc
    output_file: guide.html
'''

RETURN = r'''
# The module returns the following values:
err:
    description: The error message that asciidoctor returns when build fails..
    type: str
    returned: when build fails
'''

from ansible.module_utils.basic import AnsibleModule
import os

def run_module():
    module_args = dict(
        directory=dict(type='str', required=True),
        source_file=dict(type='str', required=True),
        output_file=dict(type='str', required=True),
        force=dict(type='bool', default=False)
    )

    result = dict(
        changed=False,
        message=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    directory = module.params["directory"]
    source_file = module.params["source_file"]
    output_file = module.params["output_file"]
    force = module.params["force"]

    if not os.path.exists("{0}".format(directory)):
        module.fail_json(name=directory, msg="ERROR (no such directory)")

    elif not os.path.exists("{0}/{1}".format(directory, source_file)):
        module.fail_json(name=source_file, msg="ERROR (no such source file)")

    elif os.path.exists("{0}/{1}".format(directory, output_file)) and force == 0:
        result['message'] = 'The {0} file already exists'.format(output_file)
        result['changed'] = False

    else:
        (rc, out, err) = module.run_command("asciidoctor -b html5 --out-file {0} {1}".format(output_file, source_file), cwd=directory)

        if err and not rc:
            result['message'] = 'The {0} file has been created with an error'.format(output_file)
            result['changed'] = True
            result['err'] = err
            module.warn(result['err'])

        elif rc == 1:
            result['err'] = err
            result['rc'] = rc
            module.fail_json(msg='Unable to create the {0} file'.format(output_file), **result)

        elif not err:
            result['message'] = 'The {0} file has been created successfully'.format(output_file)
            result['changed'] = True

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
