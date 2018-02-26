from tastypie.resources import ModelResource
from tastypie.authorization import ReadOnlyAuthorization
from sankey.models import StudentFlow


class SankeyResource(ModelResource):
	class Meta:
		resource_name = 'sankey'
		allowed_methods = ['get']
		queryset = StudentFlow.objects.all()
		filtering = {
			'flow_type': 'in',
			'department': 'exact',
			'batch': 'exact',
			'year': 'exact',
			'category': 'in'
		}
		authorization = ReadOnlyAuthorization() # default
		# always_return_data = True