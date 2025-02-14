::::::::::::::
cmd-submit-gpu-speedup-compare-ray-loop
::::::::::::::
RAY_ADDRESS='http://127.0.0.1:8265' ray job submit --working-dir test-dir -- python gpu-speedup-compare-ray-loop.py
::::::::::::::
create-manual-cluster
::::::::::::::
1) ssh to head node on cern cluster (gpu-node1)

2) Run:
ray start --head  --node-ip-address=192.168.100.1 --port=6379
IP address needed because it will use wrong interface/address

3) ssh to worker node on cern cluster (gpu-node2)

4) Run:
ray start --address=192.168.100.1:6379

this tells node where to find head node, and correctly identifies the worker's local IP address as 100.2

5) Run:
ray status
to see that both nodes are active in cluster
::::::::::::::
start_head_node
::::::::::::::
ray start --head  --node-ip-address=192.168.100.1 --port=6379
::::::::::::::
start_worker_node
::::::::::::::
ssh into worker nodem start ray there too and connected back to headnode

gpu_node2

ray start --address=192.168.100.1:6379
::::::::::::::
submit_ray_job
::::::::::::::
To run the script manually on the cluster do this on the head node:

1) Run:
RAY_ADDRESS='http://127.0.0.1:8265' ray job submit --working-dir test-dir -- python lightning_mnist_example_cpu1gpu1_gol
d.py

