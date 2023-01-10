# Techpowerup-scraper

## Scraper
The scraper makes use of scrapy to scrape the website information. The *pipelines.py* makes use of storing the items scraped in two separate csv files for gpus and cpus because they have different columns.

## CPU Dataset
The CPU dataset contains information about various CPU models and their specifications. The dataset includes the following columns:

- **Name**: The name of the CPU model.
- **Codename**: The codename used by the manufacturer for the CPU model.
- **Cores**: The number of cores in the CPU.
- **Clock**: The base clock speed of the CPU, measured in GHz.
- **Socket**: The socket type that the CPU is compatible with.
- **Process**: The manufacturing process used to create the CPU, measured in nanometers.
- **L3 Cache**: The size of the L3 cache in the CPU, measured in MB.
- **TDP**: The thermal design power of the CPU, measured in watts.
- **Released**: The release date of the CPU.
 
## GPU Dataset
The GPU dataset contains information about various GPU models and their specifications. The dataset includes the following columns:

- **Product_Name**: The name of the GPU model.
- **GPU_Chip**: The GPU Chip that is used in the GPU Model
- **Released**: The release date of the GPU.
- **Bus**: The bus width of the GPU.
- **Memory**: The memory capacity of the GPU, measured in GB.
- **GPU_clock**: The base clock speed of the GPU, measured in MHz.
- **Memory_clock**: The memory clock speed of the GPU, measured in MHz.
- **Shaders_TMUs_ROPs**: The number of shaders, texture mapping units, and raster operations pipelines in the GPU.
  
Both of the datasets are useful for comparing the performance and features of different CPU and GPU models. They can be used for a variety of applications such as gaming, content creation, AI, Machine learning, and more. It could be used by researchers to study the evolution of the technology in a specific period of time and make predictions for future advancements. It could also be used by professionals in the tech industry, to make informed decisions when choosing components for a build or a system.

The dataset updated as of January 10th,2023 can be downloaded via [kaggle](https://www.kaggle.com/datasets/baraazaid/cpu-and-gpu-stats)
