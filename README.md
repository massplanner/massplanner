massplanner

### Develpment Setup
- Clone the repository: `git clone https://github.com/massplanner/massplanner_ai.git`
- Navigate to the project directory: `cd massplanner_ai`
- Activate the virtual environment: `pipenv shell`
- Install the Python dependencies: `pipenv install`
- Build the project: `pnpm run build`
- Test the project: `pnpm run test`


| Name | Description | Dev Command |
| ----------- | ----------- | ----------- |
| recommendations:proxy_server | Required to stress test 1M+ requests | `pnpm start:recommendations:proxy_server` |