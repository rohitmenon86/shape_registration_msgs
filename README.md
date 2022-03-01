This package contains the service definition files for calling the shape registration service from other ros nodes 

# Request
Request consists of the following:
1. Observed pointcloud 

# Response
Response consists of the folowing:
1. Result of the service call back in text 
2. Result of the service call back in int format 0 for success, negative numbers for failures and positive numbers for warnings
3. Predicted point cloud 
4. Local rigid transform 

