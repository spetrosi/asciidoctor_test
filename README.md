# Role Name

This role runs asciidoctor to build AsciiDoc source files into the HTML5 format. 

## Role Variables

This role requires you to provide three variables:

### directory
Path where the AsciiDoc files that you want to build are stored.

### source_file
The filename of the AsciiDoc top level item file. For example, master.adoc.

### output_file
The filename of the HTML file that you want to build. This file will be stored in the directory provided by the directory variable.

Example of setting the variables:

```yaml
directory: "path/to/adoc/files"
source_file: "master.adoc"
output_file: "build.html"
```
## Example Playbook

```yaml
- hosts: all
  vars:
    directory: "path/to/adoc/files"
    source_file: "master.adoc"
    output_file: "build.html"

  roles:
    - linux-system-roles.asciidoctor_test

- name: Build the art-Release_Notes guide
  hosts: localhost
  vars:
    test_directory: /home/username/Documents/art-Release_Notes
  tasks:
    - name: Test the role
      import_role:
        name: asciidoctor_test
      vars:
        directory: "{{ test_directory }}"
        source_file: "master.adoc"
        output_file: "guide.html"
```

## License

MIT
