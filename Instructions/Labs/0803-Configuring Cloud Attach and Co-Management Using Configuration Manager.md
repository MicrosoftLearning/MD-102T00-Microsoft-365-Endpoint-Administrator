# Practice Lab: Configuring Cloud Attach and Co-Management Using Configuration Manager

## Summary

In this lab, you will enable Cloud Attach and configure Co-Management using Microsoft Endpoint Configuration Manager and Microsoft Intune. 

### Prerequisites

To following lab(s) must be completed before this lab:

- 0101-Managing Identities in Azure AD

- 0102-Synchronizing Identities by using Azure AD Connect

- 0201-Configuring and managing Azure AD join

- 0203-Manage Device Enrollment into Intune

### Scenario

Contoso has both a Microsoft Endpoint Configuration Manager implementation and Microsoft Intune. You need to configure integration between the two services and enable co-management for your managed Windows devices. You will enable Cloud Attach, configure co-management, and then validate the settings using SEA-CL1.

### Task 1: Prepare the environment

1. Switch to **SEA-SVR1** and sign in as **Contoso\\Administrator** with the password of **Pa55w.rd**.

2. From Server Manager, select **Tools**, and then select **Active Directory Users and Computers**.

3. In the navigation pane, select **Seattle Clients**.

4. Right-click **SEA-CL1** and then select **Move**.

5. In the **Move** dialog box, select **Azure AD clients** and then select **OK**.

6. Close **Active Directory Users and Computers**.

7. On the taskbar, right-click **Start** and select **Windows Powershell (Admin)**.

8. In the **Windows PowerShell** window, type the following command, and then press **Enter**:

```
Start-ADSyncSyncCycle -PolicyType Initial

```

9. Close the PowerShell window.

10. Switch to **SEA-CL1**.

11. On the taskbar, right-click **Start**, select **Shut down or sign out** and then select **Restart**.

    _Note: The reboot will trigger the hybrid Azure AD join on SEA-CL1._

12. After **SEA-CL1** has restarted, sign in as **Contoso\\Administrator** with the password of **Pa55w.rd**.

13. On the taskbar, right-click **Start** and select **Windows Terminal (Admin)**.

14. In the **Windows PowerShell** window, type the following command, and then press **Enter**:

```
dsregcmd /status
```

15. In the output under **Device State**, verify that **AzureAdJoined : YES** and **DomainJoined : YES** are displayed.

 _Note: If the device is not yet joined to Azure AD wait for the Azure AD Connect sync to complete and reboot SEA-CL1 again._

16. Close all windows on SEA-CL1.

### Task 2: Create a device collection

1. On **SEA-CFG1**, sign in as **Contoso\\Administrator** with the password **Pa55w.rd**.

2. On the taskbar, select **Configuration Manager Console**. The Microsoft Endpoint Configuration Manager console opens.

3. In the **Assets and Compliance** workspace, select **Device Collections**. 

4. Right-click **Device Collections** and then select **Create Device Collection**. The Create Device Collection Wizard opens.

5. On the **General** page, configure the following and then select **Next**:
   - Name: **Co-managed Devices**
   - Limiting collection: **All Desktop and Server Clients**

6. On the **Membership Rules** page, select **Next**. 

7. At the Configuration Manager warning, select **OK**. You will add a direct member at a later step.

8. On the **Summary** page, select **Next** and then at the **Completion** page, select **Close**. 

### Task 3: Assign a Device to an existing Collection

1. In the **Assets and Compliance** workspace, select **Devices**. 

   > Take note of the devices listed. Any device that has a green circle with a white checkmark are currently active.

2. In the details pane, select **SEA-CL1**.

3. Right-click **SEA-CL1**, point to **Add Selected Items**, and then select **Add Selected Items to Existing Device Collection**.

4. On the **Select Collection** dialog box, select **Co-managed Devices**, and then select **OK**.

5. To verify, in the **Assets and Compliance** workspace, select **Device Collections** and then double-click **Co-managed Devices**. 

   > SEA-CL1 should be listed as a member of this collection.

### Task 4: Cloud attach Endpoint Configuration Manager 

1. In the Microsoft Endpoint Configuration Manager console, select the **Administration** workspace.

2. In the **Administration** workspace, expand **Cloud Services** and then select **Cloud Attach**. 

3. In the ribbon, select **Configure Cloud Attach**. The **Cloud Attach Configuration Wizard** opens.

4. In the **Cloud Attach Configuration Wizard**, on the **Cloud attach** page, select **Sign In**.

5. Sign in as **`admin@yourtenant.onmicrosoft.com`** with the default tenant password. 

6. On the **Cloud attach** page, select **Customize settings**, and select **Next**.

7. On the **Create AAD Application** warning, select **Yes**.

8. On the **Configure upload** page, accept the default and select **Next**.

9. On the **Enablement** page, next to **Automatic enrollment in Intune**, select **Pilot**.

10. On the **Enablement** page, next to **Intune Auto Enrollment**, select **Browse**.

11. In the **Select Collection** dialog box, select **Co-managed Devices** and then select **OK**. Select **Next**.

12. On the **Summary** page, select **Next** and then on the **Completion** page, select **Close**.

### Task 5: Configure Workloads

1. In the Microsoft Endpoint Configuration Manager console, select the **Administration** workspace.

2. In the **Administration** workspace, expand **Cloud Services** and then select **Cloud Attach**. 

3. In the details pane, select **CoMgmtSettingsProd** and then from the ribbon select **Properties**.

   > The **CoMgmtSettingsProd Properties** box opens.

4. On the **Workloads** page, drag the slider to **Pilot Intune** for the following workloads, and then select **Next**:

   - **Compliance policies**
   - **Client apps**
   - **Windows Update policies**

5. On the **Staging** page, select **Browse** next to **Compliance policies**, **Client Apps**, and **Windows Update Policies** and select the **Co-managed Devices** collection for each workload. 

6. Select **OK** to close the **CoMgmtSettingsProd Properties** box.

### Task 6: Validate that SEA-CL1 is co-managed 

1. Switch to **SEA-SVR1**.

2. On the taskbar select **Microsoft Edge**, in the address bar type **https://aad.portal.azure.com**, and then press **Enter**.

3. Sign in as user **`Admin@yourtenant.onmicrosoft.com`**, and use the tenant Admin password. If the **Stay signed in?** prompt appears, select **No**. 

   > The Azure Active Directory admin center opens.

4. In the Azure Active Directory admin center, in the navigation pane, select **Azure Active Directory**.

5. In the **Contoso|Overview** page, under **Manage**, select **Devices**, and then select **All devices**. 

6. Verify that **SEA-CL1** is listed and that **Join Type** is **Hybrid Azure AD Join**.

7. In Microsoft Edge open another tab and type **https://endpoint.microsoft.com** in the address bar, and then press **Enter**. 

8. In the navigation pane, select **Devices** and then select **All devices**.

9. Verify that **SEA-CL1** is listed with the **Managed by** setting set to **Co-managed**. 

   > It may take some time to appear. Refresh the details pane as needed.

10. Select **SEA-CL1** and in the details pane scroll down to display information related to the Co-management state.

11. Close Microsoft Edge.

**Results**: After completing this exercise, you will have successfully enable Cloud Attach and configured co-management using Microsoft Endpoint Configuration Manager and Microsoft Intune.

**END OF LAB**
