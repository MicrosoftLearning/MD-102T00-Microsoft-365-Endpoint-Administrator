# Practice Lab04: Manage Windows Autopilot

## Summary

### Prerequisites

  > Note: You will also need a mobile phone that can receive text messages used to secure Windows Hello sign in authentication to Entra ID.

## Exercise 3: Deploying a Windows device with Autopilot

### Scenario

### Task 1: Create group in Azure AD

1. Sign in to **SEA-WS1** as **Admin** with the password **Pa55w.rd**.

2. On the taskbar, select **Microsoft Edge**.

3. In Microsoft Edge, type **https://intune.microsoft.com** in the  address bar, and then press **Enter**. 

4. Sign in as as **`admin@yourtenant.onmicrosoft.com`** with the default tenant password.

5. From the navigation pane select **Groups**, then select **New group** to start the creation of a group.

6. Enter the name **Autopilot deives** in the section **Group name**.

7. For now we do not need to a members into the group. So select **Create** to create the group. 

8. No in the group overview make sure the group was created successfully. This you can check in the top right corner by selecting the **Bell symbol** to see the notifications.

### Task 2: Generate a device-specific comma-separated value (CSV) file

1. Sign in to **SEA-WS2** as **Admin** with the password **Pa55w.rd**.

2. On the taskbar, select **Start**.

3. In the start menu, select the **Searchbar** in the top and search for **Powershell**.

4. On the right side, select **Run as Administartor**.

5. Notify the UAC request, select **Yes** to open the PowerShell.

6. Type the following lines in the PowerShell to prepare everything for the .csv generation

7. Type:  **[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12**

8. Type: **New-Item -Type Directory -Path "C:\HWID"**

9. Type: **Set-Location -Path "C:\HWID"**

10. Type: **$env:Path += ";C:\Program Files\WindowsPowerShell\Scripts"**

11. Type: **Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned**

12. Type: **Install-Script -Name Get-WindowsAutopilotInfo**

14. To now generate the .csv file type the following into the PowerShell:

13. **Get-WindowsAutopilotInfo -OutputFile AutopilotHWID.csv**

### Task 3: Work with a Windows Autopilot deployment profile


### Task 4: Reset the PC


### Task 5:Verify Autopilot deployment

**Results**: After completing this exercise, you will have successfully opend and modifyed a Windows Autopilot deployment profile to use a device name template.

**END OF LAB**