import requests, os, sys, click

uri = os.getenv('ECS_CONTAINER_METADATA_URI')

def receiver_containers():
    """ 
        Receiver containers list from your ECS instance.
    """
    r = requests.get(uri + '/task')
    data = r.json()        
    return data['Containers']


@click.command("check_containers")
def check_containers():
    """"
    Check a number of containers. If has only one, the application ends.
    """
    print("Starting ecs-verification...")

    tasks = receiver_containers()
    print(f"There's {len(tasks)} containers running!")
    if len(tasks) == 1:
        sys.exit("All containers terminated! ;)")


@click.group(help="Tool to check ECS containers.")
def _cli():
    pass

_cli.add_command(check_containers)

if __name__ == '__main__':
    _cli()
