#!/usr/bin/env python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: asciidoctor_wrapper

short_description: Build HTML output from AsciiDoc files.

version_added: "1.0.0"

description: This module uses the asciidoctor CLI tool to build AsciiDoc files into the HTML output.

options:
    directory:
        description: Defines the directory from where the asciidoctor must run.
        required: true
        type: str
    source_file:
        description: Defines the master AsciiDoc file that is used for the build.
        required: true
        type: str
    output_file:
        description: Defines the file where the HTML build is stored.
        required: true
        type: str
# Specify this value according to your collection
# in format of namespace.collection.doc_fragment_name
extends_documentation_fragment:
    - my_namespace.my_collection.my_doc_fragment_name

author:
    - Sergei Petrosian (@spetrosi)
'''

EXAMPLES = r'''
# Build the AsciiDoc files from the `/home/username/Documents/guide` directory to the guide.html file.
- name: Build HTML for `/home/username/Documents/guide`
  asciidoctor_wrapper:
    directory: "/home/username/Documents/guide"
    source_file: master.adoc
    output_file: guide.html
'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
original_message:
    description: The original name param that was passed in.
    type: str
    returned: always
    sample: 'hello world'
message:
    description: The output message that the test module generates.
    type: str
    returned: always
    sample: 'goodbye'
'''

from ansible.module_utils.basic import AnsibleModule
import os

def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        directory=dict(type='str', required=True),
        source_file=dict(type='str', required=True),
        output_file=dict(type='str', required=True)
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=False,
        original_message='',
        message=''
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    # manipulate or modify the state as needed (this is going to be the
    # part where your module will do what it needs to do)

    #command result will be 0 for success or 1 for fail
    if os.path.exists("{}/{}".format(module.params["directory"],module.params["output_file"])):
        module.exit_json(changed=False,)
        result['message'] = 'The {} file already exists'.format(module.params["output_file"])
        result['changed'] = False

    else
        module.run_command(["asciidoctor", "-b html5", "--out-file {}".format(module.params["output_fule"], "{}".format(module.params["source_file"]])
        result['message'] = 'The {} file has been created'.format(module.params["output_file"])
        result['changed'] = True

    # during the execution of the module, if there is an exception or a
    # conditional state that effectively causes a failure, run
    # AnsibleModule.fail_json() to pass in the message and the result
    # if module.params['name'] == 'fail me':
    #   module.fail_json(msg='You requested this to fail', **result)

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
