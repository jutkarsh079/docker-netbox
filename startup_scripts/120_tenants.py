from tenancy.models import Tenant, TenantGroup
from extras.models import CustomField, CustomFieldValue
from ruamel.yaml import YAML

from pathlib import Path
import sys

file = Path('/opt/netbox/initializers/tenants.yml')
if not file.is_file():
  sys.exit()

with file.open('r') as stream:
  yaml = YAML(typ='safe')
  tenants = yaml.load(stream)

  optional_assocs = {
    'group': (TenantGroup, 'name')
  }

  if tenants is not None:
    for params in tenants:
      custom_fields = params.pop('custom_fields', None)

      for assoc, details in optional_assocs.items():
        if assoc in params:
          model, field = details
          query = { field: params.pop(assoc) }

          params[assoc] = model.objects.get(**query)

      tenant, created = Tenant.objects.get_or_create(**params)

      if created:
        if custom_fields is not None:
          for cf_name, cf_value in custom_fields.items():
            custom_field = CustomField.objects.get(name=cf_name)
            custom_field_value = CustomFieldValue.objects.create(
              field=custom_field,
              obj=tenant,
              value=cf_value
            )

            tenant.custom_field_values.add(custom_field_value)

        print("👩‍💻 Created Tenant", tenant.name)
