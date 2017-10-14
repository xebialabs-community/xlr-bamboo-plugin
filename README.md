# XL Release Bamboo plugin

[![Build Status][xlr-bamboo-plugin-travis-image]][xlr-bamboo-plugin-travis-url]
[![License: MIT][xlr-bamboo-plugin-license-image]][xlr-bamboo-plugin-license-url]
![Github All Releases][xlr-bamboo-plugin-downloads-image]

[xlr-bamboo-plugin-travis-image]: https://travis-ci.org/xebialabs-community/xlr-bamboo-plugin.svg?branch=master
[xlr-bamboo-plugin-travis-url]: https://travis-ci.org/xebialabs-community/xlr-bamboo-plugin
[xlr-bamboo-plugin-license-image]: https://img.shields.io/badge/License-MIT-yellow.svg
[xlr-bamboo-plugin-license-url]: https://opensource.org/licenses/MIT
[xlr-bamboo-plugin-downloads-image]: https://img.shields.io/github/downloads/xebialabs-community/xlr-bamboo-plugin/total.svg

## Preface

This document describes the functionality provided by the XL Release Bamboo plugin.

See the [XL Release reference manual](https://docs.xebialabs.com/xl-release) for background information on XL Release and release automation concepts.

## Overview

This plugin allows XL Release to run a Bamboo plan or trigger a Bamboo deployment.

## Requirements

* XL Release 5.0+

## Installation

* Copy the latest JAR from the [releases page](https://github.com/xebialabs-community/xlr-bamboo-plugin/releases) to your `XL-RELEASE-SERVER/plugins` directory.
* Restart your XL Release server

## Usage

### RunPlan

The RunPlan.py script accepts a Bamboo project-plan-key (for example, PROJ-PLAN).  It calls Bamboo's API to run the next build job(s) for that plan and the build number is returned.  Polling of the job status occurs at 5-second intervals.  The script output will indicate the build status as success or failure.

![run-plan screenshot](images/run-plan.png)

### TriggerDeployment

The TriggerDeployment script accepts a project name, environment name, and version name.  It calls Bamboo's API to look up to respective ids of these items and then triggers a deployment. 

![trigger-deployment screenshot](images/trigger-deployment.png)

### Configuration ###

![server-configuration screenshot](images/server-configuration.png)

## References

<https://www.atlassian.com/software/bamboo>


