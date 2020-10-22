# asciidoctor_test

This role runs asciidoctor to build AsciiDoc files into the HTML5-formatted output file.

## Role Variables

This role requires you to provide three variables:

### directory
Path where the AsciiDoc file that you want to build are stored.

### source_file
The filename of the AsciiDoc file that you want to build. For example, master.adoc.

### output_file
Defines the file where the HTML build is stored.
The module creates the output file in the directory where the source file is stored.

### force
If true, recreates the HTML file even if it exists. Dafault: false.

## Example of setting the variables:

```yaml
directory: path/to/adoc/files
source_file: master.adoc
output_file: build.html
```

## Example Playbook

```yaml
- name: Build the art-Release_Notes guide
  hosts: all
  vars:
    directory: /home/Documents/art-Release_Notes
    source_file: master.adoc
    output_file: guide.html
  roles:
    - asciidoctor_test
```

## License

MIT
