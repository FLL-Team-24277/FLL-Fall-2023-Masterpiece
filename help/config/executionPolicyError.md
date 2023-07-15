To resolve the “Running scripts is disabled on this system” error, you need to change the execution policy. Follow these steps:

Launch PowerShell with administrative privileges: Click on the Start menu, type “PowerShell”, right-click on “Windows PowerShell,” and select “Run as administrator”.
Check the current execution policy: To verify the current policy, run the following command:
```
Get-ExecutionPolicy
```

Change the execution policy: To change the policy, use the `Set-ExecutionPolicy` cmdlet, followed by the desired policy. For example, to set the execution policy to RemoteSigned, run:

```
Set-ExecutionPolicy RemoteSigned
```

You will be prompted to confirm the change. Press “Y” and then Enter to confirm.

Verify the new policy: Run `Get-ExecutionPolicy` again to ensure that the policy has been changed successfully. Close and reopen the PowerShell window to apply the changes.
