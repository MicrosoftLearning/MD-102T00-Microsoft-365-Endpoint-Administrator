# Practice Lab: Deploying Windows 11 using Endpoint Configuration Manager

## Summary

In this lab, you will use Microsoft Endpoint Configuration Manager to deploy a Windows 11 Enterprise image. 

### Scenario

Contoso uses Microsoft Endpoint Configuration Manager to manage on-premises workstations. You need to refresh a Windows 8.1 computer named SEA-W81 and install the Windows 11 Enterprise operating system. You will configure the operating system deployment features of Configuration manager and deploy a task sequence to SEA-W81 to perform the operating system refresh. 

### Task 1: Create a device collection

1. On **SEA-CFG1**, sign in as **Contoso\\Administrator** with the password **Pa55w.rd**.

2. On the taskbar, select **Configuration Manager Console**. The Microsoft Endpoint Configuration Manager console opens.

3. In the **Assets and Compliance** workspace, select **Device Collections**. 

4. Right-click **Device Collections** and then select **Create Device Collection**. 

   > The Create Device Collection Wizard opens.

5. On the **General** page, configure the following and then select **Next**:
   - Name: **Windows 11 Deployment**
   - Comment: **Devices targeted to install Windows 11**
   - Limiting collection: **All Systems**

6. On the **Membership Rules** page, select **Next**. At the Configuration Manager warning, select **OK**. You will add a direct member at a later step.

7. On the **Summary** page, select **Next** and then at the **Completion** page, select **Close**. 

   > The **Windows 11 Deployment** collection is displayed in the Device Collections list.

### Task 2: Assign a Device to an existing Collection

1. In the **Assets and Compliance** workspace, select **Devices**. 

   > Take note of the devices listed. Any device that has a green circle with a white checkmark are currently active.

2. In the details pane, select **SEA-W81**.

3. Right-click **SEA-W81**, point to **Add Selected Items**, and then select **Add Selected Items to Existing Device Collection**.

4. On the **Select Collection** dialog box, select **Windows 11 Deployment**, and then select **OK**.

5. To verify, in the **Assets and Compliance** workspace, select **Device Collections** and then double-click **Windows 11 Deployment**. 

   > SEA-W81 should be listed as a member of this collection.

### Task 3: Import an Operating System Image 

1. In the Microsoft Endpoint Configuration Manager console select the **Software Library** workspace.

2. In the **Software Library** workspace, expand **Operating Systems** and then select **Operating System Images**. 

3. Right-click **Operating System Images** and then select **Add Operating System Image**. 

   > The **Add Operating System Image Wizard** displays.

4. On the **Data Source** page, select **Browse** and then browse to **\\\\sea-cfg1\\Software\\ISO\\sources\**, select **install.wim** and then choose **Open**.

5. On the **Data Source** page, select the check box next to the volume license agreement message and then select **Next**.

6. On the **Pre-cache settings** page, select the following options and then select **Next**:

   - Language: **English (United States)**
   - Architecture: **x64**

7. In the **General** page, configure the following and then select **Next**:
   - Name: **Windows 11 Enterprise**
   - Version: **21H2**

8. On the **Summary** page, select **Next**.

9. On the **Completion** page, select **Close**.

### Task 4: Distribute content to distribution points 

1. With **Operating System Images** selected, in the details pane, right-click **Windows 11 Enterprise** and then select **Distribute Content**.

2. On the **General** page, select **Next**.

3. On the **Content Destination** page, select **Add** and then select **Distribution Point**.

4. On the **Add Distribution Points** dialog box, select the check box next to **SEA-CFG1.CONTOSO.COM**, and then select **OK**.

5. On the **Content Destination** page, select **Next**.

6. On the **Summary** page, select **Next** and then select **Close**.

7. In the Ribbon, select **Refresh** and verify that the **Content Status** circle turns green and **Success** shows **1** to indicate that the content has been distributed to 1 distribution point.

### Task 5: Configure Boot Images 

1. In the Microsoft Endpoint Configuration Manager console select the **Software Library** workspace.

2. In the **Software Library** workspace, expand **Operating Systems** and then select **Boot Images**. 

   > Notice the **Boot image (x64)** and **Boot image (x86)** objects already created in the details pane. These are created when you first install Endpoint Configuration Manager.

3. Right-click **Boot image (x64)** and then select **Properties**.

4. In the **Customization** page, select the check box next to **Enable command support (testing only)** and then select **OK**.

5. At the Configuration Manager message box, select **No**. You will distribute both boot images in the next task.

### Task 6: Distribute Boot Images to distribution points 

1. With the **Boot Images** node selected, in the details pane, right-click **Boot image (x64)** and then select **Distribute Content**.

2. On the **General** page, select **Next**.

3. On the **Content Destination** page, select **Add** and then select **Distribution Point**.

4. On the **Add Distribution Points** dialog box, select the check box next to **SEA-CFG1.CONTOSO.COM**, and then select **OK**.

5. On the **Content Destination** page, select **Next**.

6. On the **Summary** page, select **Next** and then select **Close**.

7. Repeat steps 1-6 for **Boot image (x86)**.

8. Select each boot image, and then in the Ribbon, select **Refresh**. Verify that the **Content Status** circle turns green and **Success** shows **1**.

### Task 7: Create an Install image Task Sequence 

1. In the Microsoft Endpoint Configuration Manager console select the **Software Library** workspace.

2. In the **Software Library** workspace, expand **Operating Systems** and then select **Task Sequences**. 

3. Right-click **Task Sequences** and then select **Create Task Sequence**. 

   > The **Create Task Sequence Wizard** displays.

4. On the **Create a new task sequence** page, select **Install an existing image package**, and then select **Next**.

5. On the **Specify task sequence information** page, in the **Task sequence name** box, enter **Deploy Windows 11 Enterprise**.

6. Next to **Boot image**, select **Browse**.

7. In the **Select a Boot Image** dialog box, select **Boot image (x64) en-US**, and then select **OK**.

8. Select the check box next to **Run as high performance power plan,** and then select **Next**.

9. On the **Install Windows** page, select **Browse**, select **Windows 11 Enterprise 21H2 en-US**, and then select **OK**.

10. Next to **Image Index**, select **3 - Windows 10 Enterprise**. 

    > Note: The Windows 11 ISO refers to the images as Windows 10.

11. Remove the check mark next to **Configure task sequence for use with BitLocker**.

12. Select **Enable the account and specify the local administrator password**, and then in the **Password** and **Confirm password** boxes, enter **Pa55w.rd**. 

13. On the **Install Windows** page, select **Next**.

14. On the **Configure Network** page, select **Join a domain**. 

15. Next to **Domain**, select **Browse**, and then select **Contoso.com**, and then select **OK**.

16. Next to **Domain OU**, select **Browse**, and then select **Seattle Clients**, and then select **OK**.

17. On the **Specify the account that has permissions to join the domain**, select **Set**. Provide the user name **Contoso\Administrator** and the password of **Pa55w.rd** and select **OK**.

18. On the **Configure Network** page, select **Next**. 

19. On the **Install Configuration Manager** page, ensure that **Configuration Manager Client Package** is selected and then select **Next**.

20. On the **State Migration** page, remove the check mark next to **Capture user settings and files**, and then select **Next**.

21. On the **Include Updates** page, select **Do not install any software updates**, and then select **Next**.

22. On the **Install Applications** page, select **Next**.

23. On the **Summary** page, select **Next**.

24. On the **Completion** page, select **Close**.

25. Right-click the **Deploy Windows 11 Enterprise** task sequence and then select **Edit**. 

26. Under **Install Operating System**, select **Apply Device Drivers**, select the **Options** tab, and then select **Disable this step**. Select **OK**.

    > This step of the task sequence is disabled for Windows 11 compatibility. For a production deployment, you would have configured Windows 11 drivers to be installed during the deployment.

### Task 8: Deploy the Windows 11 Task Sequence

1. In the Microsoft Endpoint Configuration Manager console select the **Software Library** workspace.

2. In the **Software Library** workspace, expand **Operating Systems** and then select **Task Sequences**. 

3. In the details pane, right-click the **Deploy Windows 11 Enterprise** task sequence and then select **Deploy**.

4. On the **General** page, next to **Collection**, select **Browse**. At the warning, select **OK**.

5. Select the **Windows 11 Deployment** collection, and then select **OK**.

6. On the **General** page, select **Next**.

7. On the **Deployment Settings** page, select **Next**.

8. On the **Scheduling** page, select **Next** to make the deployment be available as soon as possible.

9. On the **User Experience** page, take note of the default settings and then select **Next**.

10. On the **Alerts** page, select **Next**.

11. On the **Distribution Points** page, select **Next**.

12. On the **Summary** page, select **Next**.

13. On the **Completion** page, select **Close**.

### Task 9: Run the Windows 11 Task Sequence

1. Switch to **SEA-W81**, and sign in as **Contoso\\Administrator** with the password of **Pa55w.rd**.

2. Select **Start** and then enter **Control Panel**.

3. In the results, select **Control Panel**.

4. In the **Control panel**, select **System and Security**.

5. In **System and Security**, select **Configuration Manager**. 

   > Configuration Manager Properties displays.

6. In the **Configuration Manager Properties** dialog box, select the **Actions** tab.

7. On the **Actions** tab, select **Machine Policy Retrieval & Evaluation Cycle**, and then select **Run Now**. At the message prompt, select **OK**.

8. Select **OK** to close the **Configuration Manager Properties**, and then close **Control Panel**. 

9. On the taskbar, in the notification area, select **New Software is Available** and then select **Open Software Center**. 

   > You might need to expand the notification area arrow to display the icon.

10. In the **Software Center**, on the **Operating Systems** page, notice the new operating system available named **Deploy Windows 11 Enterprise**. 

11. Select **Deploy Windows 11 Enterprise** and then select **Install**. 

12. On the **Confirm you want to upgrade the operating system on this computer**, select **Install**. 

    > The software will download and the task sequence begins. It will take a while to complete the install and will restart the computer as needed. Your instructor might continue with the next module while the install is taking place. Remember to come back to this lab to complete the final steps.

13. After the installation is complete, sign in as **Contoso\Administrator** with the password of **Pa55w.rd**.

14. Verify that the computer has successfully upgraded to Windows 11 and then sign out of SEA-W81.

**Results**: After completing this exercise, you will have successfully used Microsoft Endpoint Configuration Manager to deploy Windows 11.

**END OF LAB**
