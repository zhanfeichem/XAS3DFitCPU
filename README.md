# XAS3DFitCPU
XANES fit via GNN models and optimization on CPU.
This version uses the CPU-only build of PyTorch. It supports GNN model training on CPU and GNN-based XANES fitting. Although the XAS3D model has been optimized, its performance is lower than that of the CUDA version; however, it is sufficient for XAS three-dimensional structure analysis on ordinary computers without CUDA devices.
# Install
conda create -n xas3dfitcpu python=3.9
conda avtivate xas3dfitcpu
pip install Cython==3.0.11
pip install scipy==1.9.3
pip install numpy==1.23.4
pip install nlopt==2.7.1
pip install pymatgen==2022.11.7
pip install torch==1.12.1
pip install torch-cluster==1.6.0 -f https://pytorch-geometric.com/whl/torch-1.12.1%2Bcpu.html
pip install torch-scatter==2.0.9 -f https://pytorch-geometric.com/whl/torch-1.12.1%2Bcpu.html
pip install torch-sparse==0.6.15  -f https://pytorch-geometric.com/whl/torch-1.12.1%2Bcpu.html
pip install torch_geometric==2.5.3 -f https://pytorch-geometric.com/whl/torch-1.12.1%2Bcpu.html
pip install torch-spline-conv==1.2.1 -f https://pytorch-geometric.com/whl/torch-1.12.1%2Bcpu.html
# Running
Prepare the input files, including input.py, CIF files, GNN model files, etc.
python run_step1.py 
python run_step2.py
python run_step3.py
python run_step4.py



