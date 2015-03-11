# xlr-bamboo-plugin

This is a first cut at an XLR Bamboo plugin.  It provides a configuration item for a Bamboo Server and a RunPlan.py script that accepts a Bamboo project-plan-key (for example, PROJ-PLAN).  The script calls Bamboo's API to run the next build job(s) for that plan and the build number is returned.  Polling of the job status occurs at 5-second intervals.  The script output will indicate the build status as success or failure.
