clean:
				rm -rf dask-worker-space ~/scheduler.json

spawn:
				mpirun -np $$(( $$(nproc)/2 )) dask-mpi --no-nanny --scheduler-file ~/scheduler.json
