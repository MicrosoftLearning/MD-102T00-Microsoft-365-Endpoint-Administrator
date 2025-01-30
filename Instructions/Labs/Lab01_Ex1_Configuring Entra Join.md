# Practice Lab01: Configure Windows Devices in Intune

## Summary

In this lab, you will configure Entra ID Join settings and perform a standard scenario for Windows devices.

### Prerequisites

  > Note: You will also need a mobile phone that can receive text messages used to secure Windows Hello sign in authentication to Entra ID.

## Exercise 1: Configuring Entra Join

### Scenario

You need to configure Entra ID device settings to ensure that all users are allowed to join devices to Entra ID. You also need to ensure that users can only join a maximum of 20 devices and that Allan Deyoung is added as a local administrator on all Entra joined devices. Finally, you will verify that Entra join works as expected by having Joni Sherman join MD102-WS2 to the tenant.

### Task 1: Configure Entra join Device settings

1. On **MD102-WS1**, if necessary, sign in as **Contoso\\Administrator** with the password of **Pa55w.rd** and close Server Manager if necessary.

2. On the taskbar select **Microsoft Edge**, in the address bar type **https://entra.microsoft.com**, and then press **Enter**.

3. Sign in as user `Admin@yourtenant.onmicrosoft.com`, and use the tenant Admin password. If the **Stay signed in?** prompt appears, select **No**. 

   > The Microsoft Entra admin center opens.
   > You will get prompted to save your password and to sync data to Microsoft Edge. Say (No,thanks/Not now) to both of these.

4. In the Microsoft Entra admin center, in the navigation pane, expand **Identity**.

5. Select **Devices** > **All devices**.

   > Notice that there are no devices found, as you have not joined any devices yet.

6. On the **Devices | All devices** page, select **Device settings**.

7. On the **Devices|Device settings** page, in the details pane, under **Users may join devices to Microsoft Entra**, verify that **All** is selected. 

   > This indicates that all Entra users are permitted to join Windows 10 or newer devices to Microsoft Entra. Note that this setting does not apply to Entra hybrid joined devices, or devices joined by using Windows Autopilot self-deployment mode.

8. In the **Require Multi-factor Authentication to register or join devices with Microsoft Entra** section, verify that the setting is set to **No**. 

9. In the **Maximum number of devices per user** section, select **20**.

10. On the Device settings page, select **Save**.

11. Under **Local administrator settings**, select **Manage Additional local administrators on all Entra joined devices**. The Device Administrators page opens.

12. In the Device Administrators page, select **Add assignments**.

13. In the Search box, enter **Allan Deyoung**, select the **Allan Deyoung** user object, and then select **Add**. 

    > Allan Deyoung will now be added as a Device Administrator on all Entra joined devices.

14. Scroll back to or select the **Devices | Device settings** navigation link at the top of the page.

### Task 2: Perform an Entra Join

1. Switch to **MD102-WS2** and sign in as **Admin** with the password of **Pa55w.rd**.

2. On the taskbar, select **Start** and then select **Settings**.

3. In the **Settings** window, select **Accounts**.

4. On the Accounts page, select **Access work or school**.

5. In the **Access work or school** page, select **Connect**.

6. In the **Microsoft account** window, under **Alternate actions:** select **Join this device to Entra ID**.

7. On the **Sign in** page, type **JoniS@yourtenant.onmicrosoft.com** and then select **Next**.

8. On the **Enter password** page, enter the tenant password provided by your instructor and then select **Sign in**.

9.  On the **Make sure this is your organization** dialog box, select **Join**.

10. On the **You're all set!** page, select **Done**.

11. On the **Access work or school** page, verify that **Connected to Contoso's Entra ID** is displayed.

12. Close the **Settings** page.

### Task 3: Validate Entra Join

1. On MD102-WS2, right-click **Start**, and then select **Windows Terminal (Admin)**. At the User Account Control, select **Yes**.

2. In the PowerShell console, type the following and press **Enter**:

```
dsregcmd /status

```

3. In the output under **Device State**, verify that **AzureAdJoined : YES** is displayed.

   > This indicates that the device is Entra joined.

4. Close PowerShell.

5. Right-click **Start** and then select **Computer Management**.

6. In Computer Management, expand **Local Users and Groups**, and then select **Groups**.

7. Double-click the **Administrators** group.


   > Notice that Joni Sherman has been added as a local Administrator on MD102-WS2. Also notice two security principals represented by their security identifiers (SID). These two SIDs represent the Entra ID global administrator role, and the Entra joined device administrator role. 

8. Switch to **MD102-WS1**.

9. In Microsoft Edge, in the Microsoft Entra admin center, expand **Identity**.

10. Select **Devices**, and then select **All devices**. 

    > In the Devices pane, notice that MD102-WS2 is listed. 

11. Verify that the **Join Type** is listed as **Microsoft Entra joined** and that the owner is **Joni Sherman**. 

    > Also note that the MDM column shows None. This indicates that this device is not yet managed by Microsoft Intune.

### Task 4: Sign in to Windows as an Entra User

1. Switch to **MD102-WS2** and then sign in as **`JoniS@yourtenant.onmicrosoft.com`** with the Tenant password as provided by your instructor. 

   > Wait for the profile to be created.

2. At the **Use Windows Hello with your account** page, select **OK**.

3. On the **More information required** page, select **Next**.

4. On the **Keep your account secure** page, select **Next**.

5. Select **Next**, scan the QR code and **finish** the Authenticator setup.

6. On the verification page, select **Next** and then select **Done**.

7. On the **Set up a PIN** page, in the **New PIN** and **Confirm PIN** boxes, type **`102938`** and then select **OK**.

8. On the **All set!** page, select **OK**.

### Task 5: Remove a Windows device from Entra

1. On MD102-WS2, signed in as **azuread\jonisherman**, select **Start** and then select **Settings**.

2. In the **Settings** window, select **Accounts**.

3. On the Accounts page, select **Access work or school**.

4. In the **Access work or school** page, select **Connected to Contoso's Azure AD**.

5. Select **Disconnect** and then select **Yes**.

6. On the **Disconnect from the organization** page, select **Disconnect**.

7. On the **Windows Security** dialog box, in the **Email address** box, enter **Admin** and in the **Password** box, type **Pa55w.rd**. Select **OK**.

8. In the **Restart your PC** dialog box, select **Restart now**. MD102-WS2 restarts.

**Results**: After completing this exercise, you will have configured Microsoft Entra device settings, joined a device to Entra, and removed a device from Entra.

**END OF LAB**
