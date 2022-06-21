from re import template
import sys
import os
from string import Template
from hm_pyhelper.hardware_definitions import variant_definitions

# form base paths
here = os.path.dirname(os.path.abspath(__file__))
templates_folder = os.path.join(here, '../templates')
readme_filename = os.path.join(here, '../../../README.md')
balena_yml_filename = os.path.join(here, '../../../balena.yml')

# extract repository name, variant and vendor name.
REPOSITORY = sys.argv[1].split('/')[1]
VARIANT = REPOSITORY.split('_')[1]
VENDOR = VARIANT.split('-')[0]

# create template dict
template_data = {}
template_data['VARIANT_NAME'] = VARIANT
template_data['REPO_NAME'] = REPOSITORY
template_data['VENDOR'] = VENDOR
template_data['FLEET'] = f"hnt_{VARIANT}_mainnet_openfleet"
template_data['DEFAULT_DEVICE_NAME'] = variant_definitions[VARIANT]["BALENA_DEVICE_TYPE"][0]

# render templates
balena_yml_template = Template(open(os.path.join(templates_folder, 'balena.yml.template')).read())
readme_template = Template(open(os.path.join(templates_folder, 'README.md.template')).read())
balena_output = balena_yml_template.substitute(template_data)
readme_output = readme_template.substitute(template_data)

# write out the rendered data.
with open(balena_yml_filename, 'w') as f:
    f.write(balena_output)

with open(readme_filename, 'w') as f:
    f.write(readme_output)


