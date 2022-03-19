import re


class Replacer:
    def __init__(self, replaces: dict):
        """
        @replaces: dictionary of variable (key) and string to be replaced to (value)
        """
        self.replaces = replaces

    def find_variable(self, variable_name: str):
        return self.replaces.get(variable_name)

    def get_replace(self, m: re.Match):
        if m.group(1):  # TODO: Simplify this
            return self.find_variable(m.group(1))

    def use_template(self, template_path: str, replaced_path: str):
        """
        @template_path: template path
        @replaced_path: template path
        """
        with open(template_path, mode='r', encoding='utf-8') as template, \
                open(replaced_path, mode='w', encoding='utf-8') as replaced:
            for line in template:
                replaced.write(self.replace(line))

    def replace(self, line: str) -> str:
        """
        @template_path: template path
        @replaced_path: template path

        Example:

        <title>{title}</title>

        is converted to

        <title>Replaced title</title>

        End of example.
        """
        return re.sub(r'{([a-zA-Z]\w*?)}', self.get_replace, line)


repl = Replacer({
    "title": "Replaced title",
    "Heading": "Replaced heading"
})

example_template_path = '../html/template.tpl'
example_replaced_path = '../html/replaced.html'
repl.use_template(example_template_path, example_replaced_path)
