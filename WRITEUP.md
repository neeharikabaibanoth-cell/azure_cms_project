# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

### Assess app changes that would change your decision.

## Analysis of Virtual machine:
1) Cost: Higher total cost of ownership due to manual setup, maintenance, and constant resource usage
2) Scalability: Manual scaling requires load balancers and infrastructure setup
3) Availability:Must configure availability sets or zones manually
4) Workflow: Complex as ith has to SSH access, manual server setup, patching, updates
## Analysis of Azure APP Services:
1) Cost: Lower cost, especially with Free and Basic tiers; pay-as-you-go pricing
2) Scalability: Built-in auto-scaling and load balancing with minimal configuration
3) Availability:High availability is built-in and managed by Azure
4) Workflow: Streamlined CI/CD integration (e.g., GitHub), and automatic deployment support
   
Web app became my easiest option to do the project as it helped to work with ease and lead to creation of the app in a safe way.Azure App Service is the most suitable deployment option for the CMS application because it simplifies infrastructure management, reduces operational overhead, and enables fast and secure deployments. It allows developers to focus on writing and updating application code without worrying about underlying infrastructure. The platform is also cost-effective, supports automatic scaling, and integrates easily with GitHub for continuous deployment — which aligns well with modern web development workflows.

Given the CMS app's requirements — a web-based frontend, database access, file storage, and OAuth2 authentication — Azure App Service provides a fully managed Platform-as-a-Service (PaaS) solution that is secure, scalable, and production-ready with minimal configuration. It removes the need for OS management, patching, and complex setup, while still supporting environment variables, secure secret storage, and easy integration with other Azure services like SQL Database and Blob Storage. For a web app of this scale, App Service offers the best balance of simplicity, performance, and reliability.
