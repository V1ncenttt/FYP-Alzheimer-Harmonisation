<h3 align="center">Empirical comparison of neuro-imaging dataset harmonisation for Alzheimer's disease prediciton</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center">This project aims to improve the diagnosis of Alzheimer's disease (AD) and the prediction of Mild Cognitive Impairment (MCI) to AD conversion by comparing the efficiency of four post-hoc harmonisation techniques on a cohort of 1358 participants. We use neuroimaging data from the Alzheimer's Disease Neuroimaging Initiative (ADNI) dataset, and build two classifiers using cortical thickness data.
    <br> 
</p>


## Abstract

Alzheimer’s disease (AD) is a progressive neurodegenerative disease, affecting more than 55 million people worldwide. Multiple studies have shown promising results for the use of neuroimaging data for automatic prediction and diagnosis of AD. However, variations in imaging protocols and scanning devices across different studies and sites can introduce significant noise and bias in the data, making the development of reliable models challenging. Post-hoc dataset harmonisation could be a strategy to reduce variability and improve performance.

In this study, we compare the efficiency of four harmonisation techniques: ComBat, CovBat, ComBat-GAM, and NeuroHarmony, using the performance of two classifiers when trained on data harmonised with these algorithms as a metric. We assess the statistical significance of the results using the McNemar test.

Our findings show that post-hoc harmonisation is a valuable method to increase the sensitivity of AD diagnosis, but its effects are not as significant for MCI to AD conversion.

## 🏁 Getting Started <a name = "getting_started"></a>

To get started, simply run the notebooks.


### Installing

This project requires multiple python packages to run: sklearn, numpy, pandas, and the harmonisation packages.


## 🎈 Usage <a name="usage"></a>

This code can be used by other researchers to build their own framework to compare post-hoc harmonisation methods. Another potential use is to simply reuse the code to try to reproduce the results.



## ✍️ Authors <a name = "authors"></a>

- [@V1ncenttt](https://github.com/kylelobo) - Idea & Initial work
- [Dr. James Cole](https://iris.ucl.ac.uk/iris/browse/profile?upi=JCOLE07) - Project Supervisor

