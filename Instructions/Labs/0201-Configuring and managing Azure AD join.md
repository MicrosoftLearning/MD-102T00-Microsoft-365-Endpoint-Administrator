# Practice Lab 0201: Configuring and managing Entra Join

## Summary

In this lab, you will configure Entra ID Join settings and perform both standard and Entra hybrid join scenarios for Windows devices.

### Prerequisites

To following lab(s) must be completed before this lab:

- 0102-Synchronizing Identities by using Microsoft Entra Connect

  > Note: You will also need a mobile phone that can receive text messages used to secure Windows Hello sign in authentication to Entra ID.

## Exercise 1: Configuring Entra Join

### Scenario

You need to configure Entra ID device settings to ensure that all users are allowed to join devices to Entra ID. You also need to ensure that users can only join a maximum of 20 devices and that Allan Deyoung is added as a local administrator on all Entra joined devices. Finally, you will verify that Entra join works as expected by having Joni Sherman join SEA-WS1 to the tenant.

### Task 1: Configure Entra join Device settings

1. On **SEA-SVR1**, if necessary, sign in as **Contoso\\Administrator** with the password of **Pa55w.rd** and close Server Manager.

2. On the taskbar select **Microsoft Edge**, in the address bar type **https://entra.microsoft.com**, and then press **Enter**.

3. Sign in as user `Admin@yourtenant.onmicrosoft.com`, and use the tenant Admin password. If the **Stay signed in?** prompt appears, select **No**. 

   > The Microsoft Entra admin center opens.

4. In the Microsoft Entra admin center, in the navigation pane, select **Devices**, and then select **All devices**.

   > Notice that there are no devices found, as you have not joined any devices yet.

5. On the **Devices | All devices** page, select **Device settings**.

6. On the **Devices|Device settings** page, in the details pane, under **Users may join devices to Microsoft Entra**, verify that **All** is selected. 

   > This indicates that all Entra users are permitted to join Windows 10 or newer devices to Microsoft Entra. Note that this setting does not apply to Entra hybrid  joined devices, or devices joined by using Windows Autopilot self-deployment mode.

7. In the **Require Multi-factor Authentication to register or join devices with Microsoft Entra** section, verify that the setting is set to **No**. 

8. In the **Maximum number of devices per user** section, select **20**.

9. Under **Local administrator settings**, select **Manage Additional local administrators on all Entra joined devices**. The Device Administrators page opens.

10. In the Device Administrators page, select **+ Add assignments**.

11. In the Search box, enter **Allan Deyoung**, select the **Allan Deyoung** user object, and then select **Add**. 

    > Allan Deyoung will now be added as a Device Administrator on all Entra joined devices.

12. Scroll back to or select the **Devices | Device settings** navigation link at the top of the page.

13. On the Device settings page, select **Save**.

14. Select **Authentication methods**.

15. Select **SMS**.

16. Select **Enable**.

17. At the bottom of the page, select **Save**.

### Task 2: Perform an Entra Join

1. Switch to **SEA-WS1** and sign in as **Admin** with the password of **Pa55w.rd**.

2. On the taskbar, select **Start** and then select **Settings**.

3. In the **Settings** window, select **Accounts**.

4. On the Accounts page, select **Access work or school**.

5. In the **Access work or school** page, select **Connect**.

6. In the **Microsoft account** window, select **Join this device to Entra ID**.

7. On the **Sign in** page, type **JoniS@yourtenant.onmicrosoft.com** and then select **Next**.

8. On the **Enter password** page, enter the tenant password provided by your instructor and then select **Sign in**.

9. On the **Make sure this is your organization** dialog box, select **Join**.

10. On the **You're all set!** page, select **Done**.

11. On the **Access work or school** page, verify that **Connected to Contoso's Azure AD** is displayed.

12. Close the **Settings** page.

### Task 3: Validate Entra Join

1. On SEA-WS1, right-click **Start**, and then select **Windows Terminal (Admin)**. At the User Account Control, select **Yes**.

2. In the PowerShell console, type the following and press **Enter**:

   ```powershell
   dsregcmd /status
   ```

3. In the output under **Device State**, verify that **AzureAdJoined : YES** is displayed.

   > This indicates that the device is Entra joined.

4. Close PowerShell.

5. Right-click **Start** and then select **Computer Management**.

6. In Computer Management, expand **Local Users and Groups**, and then select **Groups**.

7. Double-click the **Administrators** group.

   > Notice that Joni Sherman has been added as a local Administrator on SEA-WS1. Also notice two security principals represented by their security identifiers (SID). These two SIDs represent the Entra ID global administrator role, and the Entra joined device administrator role. 

8. Close all open windows and sign out of SEA-WS1.

9. Switch to **SEA-SVR1**.

10. In Microsoft Edge, in the Microsoft Entra admin center, select **Devices**, and then select **All devices**. 

    > In the Devices pane, notice that SEA-WS1 is listed. 

11. Verify that the **Join Type** is listed as **Microsoft Entra joined** and that the owner is **Joni Sherman**. 

    > Also note that the MDM column shows None. This indicates that this device is not yet managed by Microsoft Intune.

### Task 4: Sign in to Windows as an Entra User

1. Switch to **SEA-WS1** and then sign in as **`JoniS@yourtenant.onmicrosoft.com`** with the Tenant password as provided by your instructor. 

   > Wait for the profile to be created.

2. At the **Use Windows Hello with your account** page, select **OK**.

3. On the **Let's keep your account secure** page, select **Next**.

4. On the **Keep your account secure** page, select **I want to set up a different method**.

5. In the **Choose a different method** dialog box, select **Phone** and then select **Confirm**.

6. On the **Phone** page, in the **Enter phone number** field, enter your mobile phone number which is able to receive text messages. Select **Next**.

7. When you receive the verification code, enter the code on the Phone page and then select **Next**.

8. On the verification page, select **Next** and then select **Done**.

9. On the **Set up a PIN** page, in the **New PIN** and **Confirm PIN** boxes, type **`102938`** and then select **OK**.

10. On the **All set!** page, select **OK**.

### Task 5: Remove a Windows device from Entra

1. On SEA-WS1, signed in as **azuread\jonisherman**, select **Start** and then select **Settings**.

2. In the **Settings** window, select **Accounts**.

3. On the Accounts page, select **Access work or school**.

4. In the **Access work or school** page, select **Connected to Contoso's Azure AD**.

5. Select **Disconnect** and then select **Yes**.

6. On the **Disconnect from the organization** page, select **Disconnect**.

7. On the **Windows Security** dialog box, in the **Email address** box, enter **Admin** and in the **Password** box, type **Pa55w.rd**. Select **OK**.

8. In the **Restart your PC** dialog box, select **Restart now**. SEA-WS1 restarts.

**Results**: After completing this exercise, you will have configured Microsoft Entra device settings, joined a device to Entra, and removed a device from Entra.

## Exercise 2: Configuring Entra Hybrid Join

### Scenario

Some Contoso Windows devices are currently joined to the local Active Directory Domain Services. To enable those devices to seamlessly access cloud services you plan to enable Entra hybrid join. You will test Entra hybrid join by re-configuring Entra Connect sync and testing out the process on SEA-CL2.

### Task 1: Prepare the environment

1. Switch to **SEA-SVR1**.

2. Select **Start**, expand **Windows Administrative Tools**, and then select **Active Directory Users and Computers**.

3. In **Active Directory Users and Computers**, right-click **Contoso.com**, point to **New**, and then select **Organizational Unit**.

4. In the **New-Object - Organizational Unit** dialog box, type **`Entra ID clients`** and then select **OK**.

5. In the navigation pane, select **Seattle Clients**.

6. Right-click **SEA-CL2** and then select **Move**.

7. In the **Move** dialog box, select **Entra ID clients** and then select **OK**.

8. Close **Active Directory Users and Computers**.

### Task 2: Configure Entra hybrid join in Entra Connect sync

1. On **SEA-SVR1**, on the **Desktop**, double-click **Azure AD Connect**.

2. In the **Microsoft Entra Connect Sync** window select **Configure**.

3. On the **Additional tasks** page, select **Configure device options** and select **Next**.

4. On the **Overview** page, select **Next**.

5. On the **Connect to Microsoft Entra ID** page, select **Next**.

6. On the **Sign in to your account** window, select the tenant admin account, and then enter the tenant password and select **Sign in**.

7. On the **Device options** page, select **Configure Hybrid Microsoft Entra ID join**, and then select **Next**.

8. On the **Device operating systems** page, select **Windows 10 or later domain-joined devices**, and then select **Next**.

9. On the **SCP configuration** page, select the check box next to **Contoso.com**. 

10. Select **Microsoft Entra ID** from the **Authentication Service** dropdown and select **Add**. 

11. In the **Enterprise Admin Credentials** window enter **Contoso\\Administrator** as **User name** and **Pa55w.rd** as **Password**. Select **OK** and select **Next**.

12. In the **Ready to configure** page, select **Configure** to run the configuration.

13. When the configuration is complete, select **Exit**.

14. Switch to **SEA-CL2**.

15. At the sign-in page, select the **Power** button and then select **Restart**.

    > **Note** Restarting **SEA-CL2** will enable quicker discovery of the SCP created by reconfiguring Entra Connect Sync.

16. After **SEA-CL2** has restarted, sign in as **Contoso\\Administrator** with the password of **Pa55w.rd**.

### Task 3: Re-configure Entra Connect Sync to sync the new OU

1. On **SEA-SVR1**, on the **Desktop**, double-click **Azure AD Connect**.

2. In the **Microsoft Entra Connect Sync** window select **Configure**.

3. On the **Additional tasks** page, select **Customize synchronization options** and select **Next**.

4. On the **Connect to Microsoft Entra ID** page, select **Next**.

5. One the **Sign in to your account** window, select the tenant admin account, and then enter the tenant password and select **Sign in**.

6. On the **Connect your directories** page, select **Next**.

7. On the **Domain and OU filtering** page, ensure that **Sync selected domains and OUs** is selected and then expand **Contoso.com**.

8. Select the check box next to **Entra ID clients**. **Do not make any other changes** and then select **Next**.

9. In the **Optional features** page, do not make any changes and then select **Next**.

10. In the **Ready to configure** window, select **Configure** to run the configuration and start synchronization.

11. When the configuration is complete, select **Exit**.

    > **Note**: Entra Connect Sync synchronizes automatically now when you modify the OUs being synced. You can use the **Synchronization Service** to monitor sync status.

### Task 4: Verify the Entra hybrid join

1. Switch to **SEA-CL2**.

2. Right-click **Start**, select **Shut down or sign out**, and then select **Restart**.

    _Note: The reboot will trigger the Entra hybrid join on SEA-CL2._
   
3. After **SEA-CL2** has restarted, sign in as **Contoso\\Administrator** with the password of **Pa55w.rd**.
    
4. On the taskbar, right-click **Start** and select **Windows Terminal (Admin)**.

5. In the **Windows PowerShell** window, type the following command, and then press **Enter**:

   ```powershell
   dsregcmd /status
   ```

6. In the output under **Device State**, verify that **AzureAdJoined : YES** and **DomainJoined : YES** are displayed.

   > **Note**: If the device is not yet joined to Entra ID, switch back to **SEA-SRV1** and run the command below. Once completed, switch back to SEA-CL2 and restart the computer once more.
   
   ```powershell
   Start-ADSyncSyncCycle -PolicyType Delta
   ```

7. Close all windows on SEA-CL2 and sign out.

8. Switch to **SEA-SVR1** and switch to the Microsoft Entra admin center.

9. Select **Devices** > **All devices**. 

10. Verify that **SEA-CL2** has **Microsoft Entra hybrid joined** as value for the row **Join Type**. If necessary, select the **Refresh** button if SEA-CL2 is not listed.

11. Close all windows on **SEA-SVR1**.

**Results**: After completing this exercise, you will have successfully configured and validated Entra hybrid join.

**END OF LAB**
