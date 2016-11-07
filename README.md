# Notebook


Run these notebooks in a container

```shell
docker run -d -p 8888:8888 -v ./notebooks:/notebooks -w /notebooks jseabold/dask-jupyter bash -c "jupyter notebook --no-browser --ip='*'"
```
