# Practice Lab: Configuring and managing Azure AD Join

## Summary

In this lab, you will configure Azure AD Join settings and perform both standard and hybrid Azure AD join scenarios for Windows devices.

### Prerequisites

To following lab(s) must be completed before this lab:

- 0102-Synchronizing Identities by using Azure AD Connect

  > Note: You will also need a mobile phone that can receive text messages used to secure Windows Hello sign in authentication to Azure AD.

## Exercise 1: Configuring Azure AD Join

### Scenario

You need to configure Azure Active Directory device settings to ensure that all users are allowed to join devices to Azure AD. You also need to ensure that users can only join a maximum of 20 devices and that Allan Deyoung is added as a local administrator on all Azure AD joined devices. Finally, you will verify that Azure AD join works as expected by having Joni Sherman join SEA-WS1 to the tenant.

### Task 1: Configure Azure AD join Device settings

1. On **SEA-SVR1**, if necessary, sign in as **Contoso\\Administrator** with the password of **Pa55w.rd** and close Server Manager.

2. On the taskbar select **Microsoft Edge**, in the address bar type **https://aad.portal.azure.com**, and then press **Enter**.

3. Sign in as user `Admin@yourtenant.onmicrosoft.com`, and use the tenant Admin password. If the **Stay signed in?** prompt appears, select **No**. 

   > The Azure Active Directory admin center opens.

4. In the Azure Active Directory admin center, in the navigation pane, select **Azure Active Directory**.

5. In the **Contoso|Overview** page, under **Manage**, select **Devices**. 

6. On the **Devices|Overview** page, select **All devices**. 

   > Notice that there are no devices found, as you have not joined any devices yet.

7. On the **Devices** page, select **Device settings**.

8. On the **Devices|Device settings** page, in the details pane, under **Users may join devices to Azure AD**, verify that **All** is selected. 

   > This indicates that all Azure AD users are permitted to join Windows 10 or newer devices to Azure Active Directory. Note that this setting does not apply to hybrid Azure AD joined devices, or devices joined by using Windows Autopilot self-deployment mode.

9. In the **Require Multi-factor Authentication to register or join devices with Azure AD** section, verify that the setting is set to **No**. 

10. In the **Maximum number of devices per user** section, select **20**.

11. In the **Additional local administrators on all Azure AD joined devices** section, select **Manage Additional local administrators on all Azure AD joined devices**. The Device Administrators page opens.

12. In the Device Administrators page, select **Add assignments**.

13. In the Search box, enter **Allan Deyoung**, select the **Allan Deyoung** user object, and then select **Add**. 

    > Allan Deyoung will now be added as a Device Administrator on all Azure AD joined devices.

14. Scroll back to or select the **Devices** navigation link at the top of the page.

15. On the Device settings page, select **Save**.

16. In the Azure Active Directory admin center, select **Dashboard**.

### Task 2: Perform an Azure AD Join

1. Switch to **SEA-WS1** and sign in as **Admin** with the password of **Pa55w.rd**.

2. On the taskbar, select **Start** and then select **Settings**.

3. In the **Settings** window, select **Accounts**.

4. On the Accounts page, select **Access work or school**.

5. In the **Access work or school** page, select **Connect**.

6. In the **Microsoft account** window, select **Join this device to Azure Active Directory**.

7. On the **Sign in** page, type **`JoniS@yourtenant.onmicrosoft.com`** and then select **Next**.

8. On the **Enter password** page, enter the tenant password provided by your instructor and then select **Sign in**.

9. On the **Make sure this is your organization** dialog box, select **Join**.

10. On the **You're all set!** page, select **Done**.

11. On the **Access work or school** page, verify that **Connected to Contoso's Azure AD** is displayed.

12. Close the **Settings** page.

### Task 3: Validate Azure AD Join

1. On SEA-WS1, right-click **Start**, and then select **Windows Terminal (Admin)**. At the User Account Control, select **Yes**.

2. In the PowerShell console, type the following and press **Enter**: 

```
dsregcmd /status

```

3. In the output under **Device State**, verify that **AzureAdJoined : YES** is displayed. 

   > This indicates that the device is Azure AD joined.

4. Close PowerShell.

5. Right-click **Start** and then select **Computer Management**.

6. In Computer Management, expand **Local Users and Groups**, and then select **Groups**.

7. Double-click the **Administrators** group.

   > Notice that Joni Sherman has been added as a local Administrator on SEA-WS1. Also notice two security principals represented by their security identifiers (SID). These two SIDs represent the Azure AD global administrator role, and the Azure AD joined device administrator role. 

8. Close all open windows and sign out of SEA-WS1.

9. Switch to **SEA-SVR1**.

10. In Microsoft Edge, in the Azure Active Directory admin center, select **Azure Active Directory**.

11. In the **Contoso** page, under **Manage**, select **Devices**, and then select **All devices**. 

    > In the Devices pane, notice that SEA-WS1 is listed. 

12. Verify that the **Join Type** is listed as **Azure AD joined** and that the owner is **Joni Sherman**. 

    > Also note that the MDM column shows None. This indicates that this device is not yet managed by Microsoft Intune.

13. In the Azure Active Directory admin center, select **Azure Active Directory**.

### Task 4: Sign in to Windows as an Azure AD User

1. Switch to **SEA-WS1** and then sign in as **`JoniS@yourtenant.onmicrosoft.com`** with the Tenant password as provided by your instructor. 

   > Wait for the profile to be created.

2. At the **Use Windows Hello with your account** page, select **OK**.

3. On the **More information required** page, select **Next**.

4. On the **Keep your account secure** page, select **I want to set up a different method**.

5. In the **Choose a different method** dialog box, select **Phone** and then select **Confirm**.

6. On the **Phone** page, in the **Enter phone number** field, enter your mobile phone number which is able to receive text messages. Select **Next**.

7. When you receive the verification code, enter the code on the Phone page and then select **Next**.

8. On the verification page, select **Next** and then select **Done**.

9. On the **Set up a PIN** page, in the **New PIN** and **Confirm PIN** boxes, type **102938** and then select **OK**.

10. On the **All set!** page, select **OK**.

### Task 5: Remove a Windows device from Azure AD

1. On SEA-WS1, signed in as **azuread\jonisherman**, select **Start** and then select **Settings**.

2. In the **Settings** window, select **Accounts**.

3. On the Accounts page, select **Access work or school**.

4. In the **Access work or school** page, select **Connected to Contoso's Azure AD**.

5. Select **Disconnect** and then select **Yes**.

6. On the **Disconnect from the organization** page, select **Disconnect**.

7. On the **Windows Security** dialog box, in the **Email address** box, enter **Admin** and in the **Password** box, type **Pa55w.rd**. Select **OK**.

8. In the **Restart your PC** dialog box, select **Restart now**. SEA-WS1 restarts.

**Results**: After completing this exercise, you will have configured Azure Active Directory device settings, joined a device to Azure AD, and removed a device from Azure AD.

## Exercise 2: Configuring Hybrid Azure AD Join

### Scenario

Some Contoso Windows devices are currently joined to the local Active Directory Domain Services. To enable those devices to seamlessly access cloud services you plan to enable hybrid Azure AD join. You will test hybrid Azure AD join by re-configuring Azure AD Connect and testing out the process on SEA-CL2.

### Task 1: Prepare the environment

1. Switch to **SEA-SVR1**.

2. Select **Start**, expand **Windows Administrative Tools**, and then select **Active Directory Users and Computers**.

3. In **Active Directory Users and Computers**, right-click **Contoso.com**, point to **New**, and then select **Organizational Unit**.

4. In the **New-Object - Organizational Unit** dialog box, type **Azure AD clients** and then select **OK**.

5. In the navigation pane, select **Seattle Clients**.

6. Right-click **SEA-CL2** and then select **Move**.

7. In the **Move** dialog box, select **Azure AD clients** and then select **OK**.

8. Close **Active Directory Users and Computers**.

### Task 2: Re-configure Azure AD Connect

1. On **SEA-SVR1**, on the **Desktop**, double-click **Azure AD Connect**.

2. In the **Microsoft Azure Active Directory Connect** window select **Configure**.

3. On the **Additional tasks** page, select **Customize synchronization options** and select **Next**.

4. On the **Connect to Azure AD** page enter the Admin Tenant password into the **PASSWORD** box, then select **Next**.

5. On the **Connect your directories** page, select **Next**.

6. On the **Domain and OU filtering** page, ensure that **Sync selected domains and OUs** is selected and then expand **Contoso.com**.

7. Select the check box next to **Azure AD clients**. Do not make any other changes and then select **Next**.

8. In the **Optional features** page, do not make any changes and then select **Next**.

9. In the **Ready to configure** window, select **Configure** to run the configuration and start synchronization.

10. When the configuration is complete, select **Exit**.

11. On the taskbar, right-click **Start** and select **Windows Powershell (Admin)**.

12. In the **Windows PowerShell** window, type the following command, and then press **Enter**:

```
Start-ADSyncSyncCycle -PolicyType Initial

```

13. Close the PowerShell window.

    > Wait for approximately 5 minutes for the synchronization to complete.

### Task 3: Configure hybrid Azure AD join in Azure Active Directory Connect

1. On **SEA-SVR1**, on the **Desktop**, double-click **Azure AD Connect**.

2. In the **Microsoft Azure Active Directory Connect** window select **Configure**.

3. On the **Additional tasks** page, select **Configure device options** and select **Next**.

4. On the **Overview** page, select **Next**.

5. On the **Connect to Azure AD** page, enter the Admin Tenant password into the **PASSWORD** box, then select **Next**.

6. On the **Device options** page, select **Configure Hybrid Azure AD join**, and then select **Next**.

7. On the **Device operating systems** page, select **Windows 10 or later domain-joined devices**, and then select **Next**.

8. On the **SCP configuration** page, select the check box next to **Contoso.com**. 

9. Select **Azure Active Directory** from the **Authentication Service** dropdown and select **Add**. 

10. In the **Enterprise Admin Credentials** window enter **Contoso\\Administrator** as **User name** and **Pa55w.rd** as **Password**. Select **OK** and select **Next**.

11. In the **Ready to configure** page, select **Configure** to run the configuration.

12. When the configuration is complete, select **Exit**.

13. On the taskbar, right-click **Start** and select **Windows Powershell (Admin)**.

14. In the **Windows PowerShell** window, type the following command, and then press **Enter**:

```
Start-ADSyncSyncCycle -PolicyType Initial

```

15. Close the PowerShell window.

    > Wait for approximately 5 minutes for the synchronization to complete.

### Task 4: Verify the Azure AD registration

1. Switch to **SEA-CL2**.

2. At the sign-in page, select the **Power** button and then select **Restart**.

    _Note: The reboot will trigger the hybrid Azure AD join on SEA-CL2._
   
3. After **SEA-CL2** has restarted, sign in as **Contoso\\Administrator** with the password of **Pa55w.rd**.
    
4. On the taskbar, right-click **Start** and select **Windows Terminal (Admin)**.

5. In the **Windows PowerShell** window, type the following command, and then press **Enter**:

```
dsregcmd /status
```

6. In the output under **Device State**, verify that **AzureAdJoined : YES** and **DomainJoined : YES** are displayed.

   _Note: If the device is not yet joined to Azure AD wait for the Azure AD Connect sync to complete and restart SEA-CL2 again. It might take 5-10 minutes for the status to update._

7. Close all windows on SEA-CL2 and sign out.

8. Switch to **SEA-SVR1** and switch to the Azure Active Directory admin center.

9. Select **Azure Active Directory**, and then select **Devices**. 

10. In the Devices page, select **All devices**.

11. Verify that **SEA-CL2** has **Hybrid Azure AD joined** as value for the row **Join Type**. If necessary, select the **Refresh** button if SEA-CL2 is not listed.

12. Close all windows on **SEA-SVR1**.

**Results**: After completing this exercise, you will have successfully configured and validated hybrid Azure AD join.

**END OF LAB**
