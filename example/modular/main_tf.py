region = 'us-west-2'

vpc = dict(
    source='./vpc'
)

inst = dict(
    source='./inst',
    vpc_id='${module.vpc.vpc_id}'
)

config = dict(
    provider=dict(
        aws=dict(region=region)
    ),
    module=dict(
        vpc=vpc,
        inst=inst
    )
)
