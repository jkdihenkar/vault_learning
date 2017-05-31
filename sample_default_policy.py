# as py dict
{
	'path': {
		'auth/token/lookup-self': {
			'capabilities': ['read']
		},
		'auth/token/renew-self': {
			'capabilities': ['update']
		},
		'auth/token/revoke-self': {
			'capabilities': ['update']
		},
		'sys/capabilities-self': {
			'capabilities': ['update']
		},
		'sys/renew': {
			'capabilities': ['update']
		},
		'sys/leases/renew': {
			'capabilities': ['update']
		},
		'sys/leases/lookup': {
			'capabilities': ['update']
		},
		'cubbyhole/*': {
			'capabilities': ['create', 'read', 'update', 'delete', 'list']
		},
		'sys/wrapping/wrap': {
			'capabilities': ['update']
		},
		'sys/wrapping/lookup': {
			'capabilities': ['update']
		},
		'sys/wrapping/unwrap': {
			'capabilities': ['update']
		}
	}
}
