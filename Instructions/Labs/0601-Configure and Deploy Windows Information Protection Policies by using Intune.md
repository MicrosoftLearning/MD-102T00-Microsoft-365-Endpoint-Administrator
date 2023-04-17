# Practice Lab: Configure and Deploy Windows Information Protection Policies by using Intune

## Summary

In this lab, you will configure and apply a Windows Information Protection policy to provide application protection for Windows devices that have not been enrolled into Intune.

### Prerequisites

To following lab(s) must be completed before this lab:

- 0101-Managing Identities in Azure AD

- 0102-Synchronizing Identities by using Azure AD Connect

- 0203-Manage Device Enrollment into Intune

- 0204-Enrolling devices into Intune

- 0401-Deploying cloud apps using Intune

  > Note: You will also need a mobile phone that can receive text messages used to secure Windows Hello sign in authentication to Azure AD.

### Task 1: Configure the MAM service

1. On **SEA-SVR1**, if necessary, sign in as **Contoso\\Administrator** with the password of **Pa55w.rd** and close **Server Manager**.

2. On the taskbar select **Microsoft Edge**, in the address bar type  **https://endpoint.microsoft.com**, and then press **Enter**.

3. Sign in as user **`Admin@yourtenant.onmicrosoft.com`**, and use the tenant Admin password. If the **Stay signed in?** prompt appears, select **No**. 

4. In the navigation pane, select **Devices**.

5. In the **Devices** navigation pane, select **Enroll devices**.

6. On the **Enroll devices** page, select **Automatic Enrollment**.

7. On the **Configure** page, next to **MAM user scope**, select **All**, and then select **Save**.

### Task 2: Configure an App protection policy for Windows Information Protection

1. In the Microsoft Endpoint Manager admin center, in the navigation pane, select **Apps**.

2. Select **App protection policies**, select **Create policy** and select **Windows Information Protection**.

3. In the **Name** text box, type **Windows WIP policy**.

4. In the **Enrollment state** list, select **With enrollment** and select **Next**.

5. On the **Targeted apps** tab, under **Protected apps**, select **Add**, select the following apps, and then select **OK**.

   - **Office-365-ProPlus-1810-Allowed.xml** 

   - **MsEdge - WIPMode-Allow-Enterprise AppLocker Policy File.xml**. 

6. On the **Targeted apps** tab, select **Next**.

7. On the **Required settings** tab, next to the **Windows Information Protection mode** option, select **Block** and then select **Next**. 

   > Note: Do not change the Corporate identity setting.

8. On the **Advanced settings** tab, in the **Network perimeter** section, select **Add**.

9. On the **Add network boundary** pane, configure the following, replacing **_\<yourtenantPrefix\>_** with the tenant name provided to you, and then select **OK**:

   - Boundary type: **Cloud resources**
   - Name: **SharePoint online**
   - Value: `<yourtenantPrefix>.sharepoint.com|/*AppCompat*/`

10. On the **Advanced settings** tab, next to **Show the enterprise data protection icon**, select **On** and then select **Next**.

11. On the **Assignments** tab, select **Next** and then select **Create**.

### Task 3: Deploy the policy

1. On the **Apps|App protection policies** page, in the details pane, select **Windows WIP policy**.

2. On the **Windows WIP policy** page, select **Properties**.

3. Scroll down and click **Edit** next to **Assignments**.

4. Under **Included groups** select **Add groups**, select **Research**, and then click **Select**.

5. Select **Review + save** and then select **Save**.

6. Close Microsoft Edge.

### Task 4: Refresh the policy

1. On **SEA-WS1**, sign in as **Aaron Nicholls** with the PIN: **102938**.

2. On **SEA-WS1**, on the taskbar, select **Start** and then select **Settings**.

3. In **Settings**, select **Accounts** and then select **Access work or school**.

4. In the **Access work or school** section, select the **Connected to Contoso's Azure AD** link and then select **Info**.

5. In the **Managed by Contoso** page, scroll down and then under Device sync status, select **Sync**. 

   > Wait for the synchronization to complete.

6. Close the **Settings** app. 

### Task 5: Validate the WIP Policy

*Note: It may take a while for SharePoint online to apply the Windows Information Policy. If , after a while, you do not see the WIP indicator in step 2, skip to Task 6 for an alternate task to test WIP.*

1. On the taskbar, select **Microsoft Edge**.

2. Open **Microsoft Edge**, and navigate to `https://yourtenant.sharepoint.com`.

   > Take note of the briefcase icon at the right side of the address bar. Select the icon and verify that this website is managed by the tenant. It may take a while for the briefcase icon to appear. If it does not appear after 5 minutes, skip to Task 6 to complete the alternate task to test WIP.

3. Under the **Communication Site** heading, select **Documents**.

4. On the **Documents** page, select **New** and then select **Word Document**.

5. In the **Your privacy option** prompt, select **Close**.

6. In the Word document, type **This is a sample document** and then close the Document.docx tab. 

   > The file saves automatically to the Documents library in SharePoint.

7. Select **Document.docx** and select **Download**.

8. On the taskbar, open **File Explorer** and browse to the **Downloads** folder.

*Note: The briefcase icon in the file icon indicates that the file is protected.*

9. Open the **Document.docx** file using **Word**. The file should open because Word is a managed app indicated in the policy. 

10. Right-click **Start** and then select **Task Manager**.

11. In Task Manager, select **More details**, and then select the **Details** tab.

12. Right-click the column headings and then click **Select columns**.

13. In the **Select columns** dialog box, select the check box next to **Enterprise context**, and then select **OK**.

    > Notice that msedge.exe and WINWORD.EXE both have the Enterprise context that states your Tenantname and that both apps are Enlightened and Permissive.

14. Click **Start** and then select **Notepad**.

15. Switch to **Word** and attempt to copy and paste text from Word into Notepad. 

    > Notice that you are prevented from pasting content from Word into Notepad.

16. Switch to **Task Manager**, and on the **Details** tab look for **Notepad.exe**.

17. Validate the Enterprise context of Notepad.exe.

    > Notice that the Enterprise context for Notepad.exe is Personal. Windows Information Protection will not allow you to copy and paste information between an app that is considered a workplace app and a personal app.

18. Close all open windows and sign out of SEA-WS1.

### Task 6: Compare Enlightened and Unenlightened Apps (Alternate Task)

1. Click **Start** and then select **Word**.

2. In Word, select **Blank document**.

3. In the Word document, type **This is a sample document**.

4. Select **File**, and then select **Save As**.

5. On the **Save As** page, select **This PC**.

6. In the **Enter file name here** box, enter **Sample Document**, and then select **Save**.

7. Close **Word**.

8. On the taskbar, open **File Explorer** and browse to the **Documents** folder.

9. Right-click **Sample Document**, and then select **Show more options**.

10. Select **File ownership** and then select **Work**.

    > Notice that the document now has a briefcase icon attached to indicate that this is a work document. Also the File ownership column indicates the Tenant name.

11. Open the **Sample Document** file using **Word**. The file should open because Word is a managed app indicated in the policy. 

12. Right-click **Start** and then select **Task Manager**.

13. In Task Manager, select **More details**, and then select the **Details** tab.

14. Right-click the column headings and then click **Select columns**.

15. In the **Select columns** dialog box, select the check box next to **Enterprise context**, and then select **OK**.

    > Notice that msedge.exe and WINWORD.EXE both have the Enterprise context that states your Tenantname and that both apps are Enlightened and Permissive.

16. Click **Start** and then select **Notepad**.

17. Switch to **Word** and attempt to copy and paste text from Word into Notepad. 

    > Notice that you are prevented from pasting content from Word into Notepad.

18. Switch to **Task Manager**, and on the **Details** tab look for **Notepad.exe**.

19. Validate the Enterprise context of Notepad.exe.

    > Notice that the Enterprise context for Notepad.exe is Personal. Windows Information Protection will not allow you to copy and paste information between an app that is considered a workplace app and a personal app.

20. Close all open windows and sign out of SEA-WS1.

**Results**: After completing this exercise, you will have successfully configured a Windows Information Protection policy to provide data protection.

**END OF LAB**
