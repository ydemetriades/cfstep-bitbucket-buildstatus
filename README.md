# Bitbucket Build Status

## Description:
This plugin enables Codefresh Pipelines to update the Build Status of a commit in Bitbucket Cloud or Bitbucket Server.

Can be used to trigger pipelines for CI, Pull Request merge check etc.

## Usage

In this section will find the available Parameters and Examples.

The following examples are using the `ydemetriades/bitbucket-buildstatus` Codefresh step available in [Marketplace](https://codefresh.io/steps/step/ydemetriades%2Fbitbucket-buildstatus)

### Parameters

Both, Codefresh step and docker image, are configurable through parameters in order to perform the action.

|Name|Required|Description|Available Options|
|----|--------|-----------|-----------------|
|BB_BSN_URL|Yes|Bitbucket Server API Url|-|
|BB_BSN_REPO_AUTH_USER|Yes|Bitbucket Server API Authorization Username|-|
|BB_BSN_REPO_AUTH_PASSWORD|Yes|Bitbucket Server API Authorization Password|-|
|CF_BUILD_STATUS|Yes|Build Status|`SUCCESSFUL` `FAILED` `INPROGRESS` `STOPPED`|

### Example

```yaml
version: '1.0'
steps:
  BB_Update_BuildStatus:
    type: ydemetriades/bitbucket-buildstatus
    arguments:
      BB_BSN_URL: ${{BB_BSN_URL}}
      BB_BSN_REPO_AUTH_USER: ${{BB_BSN_REPO_AUTH_USER}}
      BB_BSN_REPO_AUTH_PASSWORD: ${{BB_BSN_REPO_AUTH_PASSWORD}}
      CF_BUILD_STATUS: ${{CF_BUILD_STATUS}}
```

### Advanced Example

```yaml
version: '1.0'
mode: parallel
steps:
  BB_Update_BuildStatus_InProgress:
    type: ydemetriades/bitbucket-buildstatus
    fail_fast: false
    arguments:
      BB_BSN_URL: ${{BB_BSN_URL}}
      BB_BSN_REPO_AUTH_USER: ${{BB_BSN_REPO_AUTH_USER}}
      BB_BSN_REPO_AUTH_PASSWORD: ${{BB_BSN_REPO_AUTH_PASSWORD}}
      CF_BUILD_STATUS: 'INPROGRESS'

    ## [Some more steps...]

    BB_Update_BuildStatus_Finished:
    type: parallel
    fail_fast: false
    when:
      condition:
        all:
          myCondition: workflow.result == 'finished'
    steps:
      BB_Update_BuildStatus_Successful:
        type: ydemetriades/bitbucket-buildstatus
        when:
          condition:
            all:
              myCondition: workflow.result == 'success'
        arguments:
          BB_BSN_URL: ${{BB_BSN_URL}}
          BB_BSN_REPO_AUTH_USER: ${{BB_BSN_REPO_AUTH_USER}}
          BB_BSN_REPO_AUTH_PASSWORD: ${{BB_BSN_REPO_AUTH_PASSWORD}}
          CF_BUILD_STATUS: 'SUCCESSFULL'
      BB_Update_BuildStatus_Failed:
        type: ydemetriades/bitbucket-buildstatus
        when:
          condition:
            all:
              myCondition: workflow.result == 'failure'
        arguments:
          BB_BSN_URL: ${{BB_BSN_URL}}
          BB_BSN_REPO_AUTH_USER: ${{BB_BSN_REPO_AUTH_USER}}
          BB_BSN_REPO_AUTH_PASSWORD: ${{BB_BSN_REPO_AUTH_PASSWORD}}
          CF_BUILD_STATUS: 'FAILED'
```

## Maintainers


[Yiannis Demetriades](https://github.com/ydemetriades)
