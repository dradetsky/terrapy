default_vpc = dict(
    enable_dns_hostnames=True,
    cidr_block='10.0.0.0/16',
    tags={'Name': 'default'},
)
default_gateway = dict(vpc_id='${aws_vpc.default.id}')
internet_access_route = dict(
    route_table_id='${aws_vpc.default.main_route_table_id}',
    destination_cidr_block='0.0.0.0/0',
    gateway_id='${aws_internet_gateway.default.id}'

)

vpc_id = dict(
    value='${aws_vpc.default.id}'
)

config = dict(
    resource=dict(
        aws_vpc=dict(default=default_vpc),
        aws_internet_gateway=dict(default=default_gateway),
        aws_route=dict(internet_access=internet_access_route),
    ),
    output=dict(
        vpc_id=vpc_id
    )
)
