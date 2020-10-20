# Role Name

This role runs asciidoctor to build AsciiDoc source files into the HTML5 format. 

## Requirements

Any pre-requisites that may not be covered by Ansible itself or the role should
be mentioned here. For instance, if the role uses the EC2 module, it may be a
good idea to mention in this section that the `boto` package is required.

## Role Variables

A description of all input variables (i.e. variables that are defined in
`defaults/main.yml`) for the role should go here as these form an API of the
role.

Variables that are not intended as input, like variables defined in
`vars/main.yml`, variables that are read from other roles and/or the global
scope (ie. hostvars, group vars, etc.) can be also mentioned here but keep in
mind that as these are probably not part of the role API they may change during
the lifetime.

Example of setting the variables:

```yaml
directory: "path/to/adoc/files"
source_file: "master.adoc"
output_file: "build.html"
```

### Variables Exported by the Role

This section is optional.  Some roles may export variables for playbooks to
use later.  These are analogous to "return values" in Ansible modules.  For
example, if a role performs some action that will require a system reboot, but
the user wants to defer the reboot, the role might set a variable like
`template_reboot_needed: true` that the playbook can use to reboot at a more
convenient time.

Example:

`template_reboot_needed` - default `false` - if `true`, this means
a reboot is needed to apply the changes made by the role

## Dependencies

A list of other roles hosted on Galaxy should go here, plus any details in
regards to parameters that may need to be set for other roles, or variables
that are used from other roles.

## Example Playbook

```yaml
- hosts: all
  vars:
    directory: "path/to/adoc/files"
    source_file: "master.adoc"
    output_file: "build.html"

  roles:
    - linux-system-roles.asciidoctor_test
```

## License

MIT

## Author Information

An optional section for the role authors to include contact information, or a
website (HTML is not allowed).
