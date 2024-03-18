OMP_NUM_THREADS=32 numactl --physcpubind=0-31 --membind=0 python pysparkai_sqlcoder.py --n=1 --num-prompts=1000 --dtype=bfloat16 --trust-remote-code --device=cpu--swap-space=40
