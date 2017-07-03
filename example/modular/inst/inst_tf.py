example_inst = dict(
    tags={'Name': 'example_inst'},
    connection={'user': 'ubuntu'},
    instance_type='t2.small',
    ami='ami-efd0428f',
)

config = dict(
    variable=dict(
        vpc_id={}
    ),
    resource=dict(
        aws_instance=dict(
            example_inst=example_inst
        )
    )
)
