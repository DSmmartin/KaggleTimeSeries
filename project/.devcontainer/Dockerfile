FROM ubuntu:16.04 as builder

RUN apt-get update && apt-get -y install --no-install-recommends apt-utils 2>&1 \
    wget \
    libdigest-sha-perl \
    bzip2
RUN apt-get -y install git procps lsb-release
RUN apt-get install -y libicu[0-9][0-9]

RUN wget --quiet --output-document miniconda.sh https://repo.continuum.io/miniconda/Miniconda3-4.5.12-Linux-x86_64.sh \
    && (echo '866ae9dff53ad0874e1d1a60b1ad1ef8  miniconda.sh' | md5sum -c) \
    && (echo 'e5e5b4cd2a918e0e96b395534222773f7241dc59d776db1b9f7fedfcb489157a  miniconda.sh' | shasum -a 256 -c) \
    && /bin/bash miniconda.sh -b -p /databricks/conda \
    && rm miniconda.sh \
    && /databricks/conda/bin/conda install --name base conda=4.6.12

FROM databricksruntime/minimal

COPY --from=builder /databricks/conda /databricks/conda

COPY conda_dependencies.yml /databricks/.conda-env-def/conda_dependencies.yml

RUN /databricks/conda/bin/conda env create --file /databricks/.conda-env-def/conda_dependencies.yml \
    && ln -s /databricks/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh

RUN /databricks/conda/bin/conda config --system --set channel_priority strict \
    && /databricks/conda/bin/conda config --system --set always_yes True

ENV DEFAULT_DATABRICKS_ROOT_CONDA_ENV=kaggle_web_traffic_forecasting
ENV DATABRICKS_ROOT_CONDA_ENV=kaggle_web_traffic_forecasting