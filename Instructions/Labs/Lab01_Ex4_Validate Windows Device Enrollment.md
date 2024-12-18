# Practice Lab01: Configure Windows Devices in Intune

## Summary

In this lab, you will join a Windows client to Entra ID and verify that the device has automatically enrolled in to Microsoft Intune.

### Prerequisites

  > Note: You will also need a mobile phone that can receive text messages used to secure Windows Hello sign in authentication to Entra ID.
## Exercise 4: Validate Window Device enrollment

### Scenario

You have assigned Megan Bowen appropriate licenses and will now test the process of joining a Windows device to Entra ID and have it automatically enroll in Microsoft Intune.

### Task 1: Automatically enroll a Windows device to Microsoft Intune

1. Sign in to **MD102-WS2** as **Admin** with the password of **Pa55w.rd**.

2. Select **Start** and then select **Settings**.

3. In **Settings**, select **Accounts**.

4. On the Accounts page, select **Access work or school**.

5. In the **Access work or school** page, select **Connect**.

6. In the **Microsoft account** window, under **Alternate actions:** select **Join this device to Microsoft Entra ID**.

7. On the **Sign in** page, type **`MeganB@yourtenant.onmicrosoft.com`** and then select **Next**.

8. On the **Enter password** page, enter the tenant password provided by your instructor and then select **Sign in**.

9. On the **Make sure this is your organization** dialog box, select **Join**.

10. On the **You're all set!** page, read the information and then select **Done**.

11. In the **Access work or school** section, verify that **Connected to Contoso's Entra ID** displays.

12. Select **Connected to Contoso's Azure AD** and then select **Info**.

13. Take note of the information regarding the areas managed by Contoso, scroll down, and then select **Sync**. This will force a Device sync with Intune.

14. Close the **Settings** window.

### Task 2: Validate device enrollment into Entra ID And Intune

1. On the **MD102-WS2** taskbar, select **Start**, type **cert**, and select **Manage computer certificates**.
    
2. In the **Certificates** console, in the navigation pane, expand **Personal** and select the **Certificate** node. Verify that the following certificates are listed in the details pane:

-   Microsoft Intune MDM Device CA
-   MS-Organization-Access
-   MS-Organization-P2P-Access \[2024\]

    This indicates that the device is enrolled in Entra ID and Intune.

3. Close the Certificates window.

4. Right-click **Start**, and then select **Windows Terminal (Admin)**. When prompted select **Yes**.

5. In the PowerShell console, type the following and press **Enter**: 

```
dsregcmd /status
```

6. In the output under **Device State**, verify that **AzureADJoined : YES** is displayed. This indicates that the device is Entra ID joined.

7. In the output under **Tenant Details**, verify that the following three entries exist:

```
mdmUrl : https://enrollment.manage.microsoft.com/enrollmentserver/discovery.svc
mdmTouUrl : https://portal.manage.microsoft.com/TermsofUse.aspx
mdmComplianceUrl : https://portal.manage.microsoft.com/?portalAction=Compliance
```

> Note: These entries indicate that the device is enrolled in Intune.

### Task 3: Sign in as an Entra user

1. Sign out of **MD102-WS2**.

2. Select **Other user**, and sign in as **`MeganB@yourtenant.onmicrosoft.com`**. Wait for the profile to be created.

3. At the **Use Windows Hello with your account** page, select **OK**.

4. On the **More information required** page, select **Next**.

5. On the **Keep your account secure** page, select **Next**.

6. Select **Next**, scan the QR code and **finish** the Authenticator setup.

7. On the verification page, select **Next** and then select **Done**.

8.  On the **Set up a PIN** page, in the **New PIN** and **Confirm PIN** boxes, type **102938** and then select **OK**.

9.  On the **All set!** page, select **OK**.

10. Sign out of **MD102-WS2**.

### Task 4: Verifying device enrollment in the Intune console

1. Switch to **MD102-WS1** as **Contoso\Administrator** with the password of **Pa55w.rd**. 

2. In Microsoft Edge, type **https://intune.microsoft.com** in the address bar, and then press **Enter**. Sign in with your Tenant administrator account.

3. In the navigation pane, select **Devices**.

4. On the **Devices | Overview** blade under **Intune enrolled devices**, verify that **1** is displayed next to **Windows**. It may take a while to display.

5. On the **Devices | Overview** blade, select **All devices** and verify that **MD102-WS2** is listed.

6. Note that for MD102-WS2, the **Managed by** column displays **Intune** and the **Ownership** column displays **Corporate**. 

   _Note: This view lists devices that are enrolled to Intune. Remember that you configured automatic enrollment between Entra and Intune, and because of that, any device that is joined or registered to Entra is automatically enrolled to Intune. Any devices joined prior to setting up enrollment are only joined or registered to Entra, but not enrolled in Intune._

7. Open a new tab in **Microsoft Edge**, in the address bar type **https://entra.microsoft.com**, and then press **Enter**.

8. In the Microsoft Entra admin center, expand **Identity**.

9. Select **Devices**, then select **All devices**. 

   > Take note of MD102-WS2. Notice that the Join Type column displays **Microsoft Entra joined** and the MDM column displays **Microsoft Intune**.

10. Close all open Windows.

### Task 5: Getting more Information about the enrolled device and user

1. On **MD102-WS1**, on the taskbar, select **Microsoft Edge**.

2. In Microsoft Edge, type **https://intune.microsoft.com** in the address bar, and then press **Enter**.

3. Sign in as **`admin@yourtenant.onmicrosoft.com`** with the tenant Admin password.

4. On the **Microsoft Intune admin center** page, select **Users**.

5. On the **Users|All users** pane, select **Sign-ins logs**.

6. In the Details pane, user sign-ins are listed. Select the first entry where the **User** column displays **Megan Bowen**.

7. In the **Details** pane, Megan Bowen´sign-in details are displayed.

8. Select each of the main pages, including **Basic info**, **Location**, **Device info**, **Authentication Details**, and **Conditional Access**. Scroll to examine information on each page and then select **X** in the top right hand corner to close out of the **Activity Details** page.

9. In the Users navigation pane, select **Audit logs**.

10. In the details pane, audit information is displayed about administrative changes to users. Examine the information by selecting the various entries.

**Results**: After completing this exercise, you will have successfully joined a Windows client to Entra ID. verified that the device has automatically enrolled in to Microsoft Intune and get informations about the enrolled Device and user.

**END OF LAB**
