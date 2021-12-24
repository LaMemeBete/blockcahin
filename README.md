### Brownie

## Brownie managing accounts

Add account: brownie accounts new [account-name]
View list of accounts: brownie accounts list

## Brownie Testing

Run script (file dhould be in scripts folder): brownie run [file-name.py]
Run tests: brownie test
Select specific test to test in brownie: brownie test -k [function-name]
To open dynamic shell while testing: brownie test --pdb
More output and option to print stff during tests: brownie test -s
To see more info about how testing works in brownie refer to docs.pytest.org

## Brownie blockchain networks

Run on a specific test account: brownie run scripts/deploy.py --networks rinkeby
Run on local instance: brownie run scripts/deploy.py

## Brownie console

Enter interactive mode with brownie: brownie console