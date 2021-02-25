import requests, os, time, sys

uri = os.getenv('ECS_CONTAINER_METADATA_URI')

def receiver_containers():
    """ 
        Receiver containers list from your ECS instance.
    """
    r = requests.get(uri + '/task')
    data = r.json()        
    return data['Containers']

def check_containers():
    """"
        Check a number of containers. If has only one, the application ends.
    """
    tasks = receiver_containers()

    if len(tasks) == 1:
        sys.exit("All containers terminated! ;)")
    print(f"There's {len(tasks)} containers running!")

print("Starting ecs-verification...")
print(f'AWS ECS url: {uri}')
while True:
    check_containers()
    time.sleep(60)
