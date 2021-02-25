import requests, os, sys, click, signal, time

uri = os.getenv('ECS_CONTAINER_METADATA_URI')

def receiver_containers():
    """ 
        Receiver containers list from your ECS instance.
    """
    r = requests.get(uri + '/task')
    data = r.json()   

    return data['Containers']

def count_running_containers(tasks):
    count = 0
    for container in tasks:
        if container['KnownStatus'] == "RUNNING":
            count += 1
    return count


@click.command("check_containers")
def check_containers():
    """"
    Check a number of containers. If has only one, the application ends.
    """
    tasks = receiver_containers()
    running_containers = count_running_containers(tasks)
    
    if running_containers == 1:
        print("All containers terminated! ;)")
    else:
        print(f"There's {running_containers} containers running!")


@click.group(help="Tool to check ECS containers.")
def _cli():
    pass

_cli.add_command(check_containers)

if __name__ == '__main__':
    _cli()
