# Practice Lab 0203: Manage Device Enrollment into Intune

## Summary

In this lab, you prepare for device management using Microsoft Intune by reviewing and assigning licenses, configuring Windows automatic enrollment, and configuring enrollment restrictions. 

### Prerequisites

To following lab(s) must be completed before this lab:

- 0101-Managing Identities in Entra ID

- 0102-Synchronizing identities by using Entra Connect

  > Note: You will also need a mobile phone that can receive text messages used to secure Windows Hello sign in authentication to Entra ID.

### Scenario

You need to prepare for device management using Microsoft Intune. First of all, you need to ensure that users are assigned appropriate licenses for device management. As a verification test, you will assign Aaron Nicholls the required licenses. You also need to ensure that any Windows device that is joined or registered to Entra ID will automatically be enrolled into Intune. You have also been asked to ensure that members of the Sales group are restricted from enrolling personal Android devices into Intune and that the Enrollment Device Limit is increased to 10 devices. Finally, you need to configure Allan Deyoung as a Device enrollment manager to allow him to enroll 1000 devices.

### Task 1: Review and assign licenses for device management

1. On **SEA-SVR1**, if necessary, sign in as **Contoso\\Administrator** with the password of **Pa55w.rd** and close **Server Manager**.

2. On the taskbar select **Microsoft Edge**, in the address bar type **https://admin.microsoft.com**, and then press **Enter**.

3. Sign in as user `Admin@yourtenant.onmicrosoft.com`, and use the tenant Admin password. If the **Stay signed in?** prompt appears, select **No**. 

   > The Microsoft 365 admin center opens.

4. In the Microsoft 365 admin center navigation pane, select **Users** > **Active users**.

5. Select **Aaron Nicholls** (select the name, not the checkbox).

6. Select the **Licenses and apps** tab.

7. If the **Select location** field is not populated, select the a location from the drop-down list.

8. Select the check boxes next to **Enterprise Mobility + Security E5** and **Office 365 E5 (no Teams)**.

9. Select **Save Changes**.

10. Once the changes have been saved, close the **Microsoft 365 admin center** tab in Edge. 


### Task 2: Enable Windows Automatic Enrollment into Microsoft Intune

1. In **SEA-SVR1**, open a new tab in **Microsoft Edge**, and then in the address bar type **https://intune.microsoft.com**, and then press **Enter**. 

   > The Microsoft Intune admin center opens.

2. In the Microsoft Intune admin center, select **Devices**.

3. On the Devices pane, under the **Device onboarding** section, select **Enrollment**.

4. In the Enroll devices pane, ensure **Windows** is selected.

5. In the **Enrollment options** section, select **Automatic Enrollment**.

6. On the **MDM user scope** row, select **All** and then select **Save**.

   _**Note**: By performing this step, you enabled automatic enrollment into Intune for any User that performs an Entra join or Entra registration from a Windows device._

### Task 3: Configure Enrollment Restrictions

1. In the Microsoft Intune admin center, select **Devices**.

2. On the Devices pane, under the **Device onboarding** section, select **Enrollment**.

3. On the **Devices | Enrollment** page, in the **Enrollment options** section, note that you can create enrollment device limit and platform restrictions. 

4. Select **Device platform restriction**. 

   > Notice that there is a Default device type restriction that is assigned to **All Users**. This default restriction allows all device types.

5. In the details pane, select the **Android restrictions** tab, and then select **+ Create restriction**.

6. On the Create restriction page, in the Name box enter **Android Personal Device Restriction**. Select **Next**.

7. On the Device limit page, select **Next**.

8. On the Scope tags page, select **Next**.

9. On the Assignments page, under Included groups, select **Add groups**.

10. Search for and Select **Sales** and then click **Select** and then click **Next**.

11. On the **Review + create** page, select **Create**.

    > Notice the Android Personal Device Restriction assigned with a priority of 1.

12. On the **Enrollment** pane, select **Device limit restrictions**. 

    > Notice that there is a Default device limit restriction that is assigned to **All Users**. This default restriction sets a device enrollment limit to 5 devices per user.

13. In the details pane, select **+ Create restriction**.

14. On the Create restriction page, in the Name box enter **Sales Device Enrollment Limit**. Select **Next**.

15. On the Device limit page, select **10** and then select **Next**.

16. On the Scope tags page, select **Next**.

17. On the Assignments page, under Included groups, select **Add groups**.

18. Search for and Select **Sales** and then click **Select** and then click **Next**.

19. On the **Review + create** page, select **Create**.

    > Notice the Sales Device Enrollment Limit, configured with a Device limit of 10 and assigned with a priority of 1.

### Task 4: Configure a Device enrollment manager

1. In the Microsoft Intune admin center, select **Devices**.

2. On the Devices pane, select **Enrollment**.

3. On the **Enroll devices** pane, select **Device enrollment managers**. 

   > Notice that, by default, there are no Device enrollment managers configured.

4. On the **Devices|Device enrollment managers** page, select **+ Add**.

5. In the **Add user** page, under User name, enter `AllanD@yourtenant.onmicrosoft.com` and then select **Add**.

   > Allan is now allowed to enroll up to 1000 devices.

6. In the Microsoft Intune admin center, in the navigation pane, select **Home**.

7. Close Microsoft Edge.

**Results**: After completing this exercise, you will have successfully reviewed and assigned licenses, configured Windows automatic enrollment, enabled and assigned enrollment restrictions, and configured a Device enrollment manager.


**END OF LAB**
