---
lab:
  title: 'Lab 01: Foundation — Identity, enrollment, and Autopilot'
  description: 'In this lab, you configure Microsoft Entra ID identity governance, device registration and enrollment policies, and Windows Autopilot to prepare a Microsoft 365 tenant for Intune device management.'
  duration: 90 minutes
  level: 200
  islab: true
  primarytopics:
    - Microsoft Intune
    - Microsoft Entra ID
    - Windows
    - Windows Autopilot
---

# Lab 01: Foundation — Identity, enrollment, and Autopilot

## Lab scenario

You are **Jordan Chen**, Modern Endpoint Administrator at Contoso Healthcare. Contoso is adopting a cloud-first endpoint management strategy using Microsoft Intune and Microsoft Entra ID. Your first task is to prepare the Microsoft 365 tenant for device management by configuring identity governance (users, groups, and roles), device registration policies, Windows enrollment policies, and Windows Autopilot. This foundational configuration will enable the device enrollment and policy deployment work in subsequent labs.

By the end of this lab, you'll have:
- Configured users and dynamic groups (including a compound-rule dynamic group) for organizational targeting
- Delegated administrative access using Microsoft Entra ID roles, administrative units, and a custom Intune RBAC role with a scope tag
- Set device registration policies and enabled Microsoft Entra Local Administrator Password Solution (LAPS)
- Verified automatic Intune enrollment and configured Enrollment Status Page profiles
- Blocked personally owned Android device enrollment
- Enrolled two Windows 11 devices via Microsoft Entra join
- Registered a device for Windows Autopilot with a deployment profile

---

## Lab Duration

**Estimated Time:** 90 minutes

---

## Instructions

### Before you begin

This lab requires:
- Access to the Contoso Microsoft 365 tenant (`<TenantPrefix>.onmicrosoft.com` or equivalent)
- Global Administrator credentials
- Four virtual machines: **SEA-DEV1**, **SEA-DEV2**, **SEA-DEV3**, and **LIN-SRV1**
- Internet connectivity from all VMs

**Important:** This is the foundational lab for the MD-102 lab series. All subsequent labs assume the configuration completed in this lab (enrolled devices, users, groups, and policies).

> [!IMPORTANT]
> **Complete multifactor authentication (MFA) enrollment before starting Exercise 2.** Some Contoso lab tenants have a Conditional Access policy that enforces the `p1` (MFA) authentication context for the Azure management API. This blocks access to **entra.microsoft.com** and **intune.microsoft.com** until your admin account is enrolled in MFA. The Microsoft 365 admin center (**admin.cloud.microsoft**) is exempt and works without MFA. If you're prompted to set up additional security verification on first sign-in, complete the Microsoft Authenticator setup before continuing.
>
> The Microsoft 365 admin center may open in **Simplified view** by default. Switch to **Dashboard view** from the toggle in the top-right corner to match the screenshots in this lab.

---

> [!IMPORTANT]
> **Activate the Microsoft Intune Suite 90-day trial now — before you start Lab 03.** Several later exercises (Lab 03 Exercise 4, Lab 04 Exercises 4–5, Lab 06 Exercises 1–3) require Intune Suite capabilities. Activating the trial up front means every downstream lab “just works” and avoids surprise blockers mid-lab. The trial is free, 90 days, up to 250 users per tenant, and reuses your existing tenant billing relationship — no payment method is required.
>
> **Steps (takes about two minutes):**
>
> 1. In the **Microsoft Intune admin center** (`intune.microsoft.com`), select **Tenant administration** and then select **Intune add-ons**.
> 2. Select the **All add-ons** tab.
> 3. In the row for **Microsoft Intune Suite**, under the **Try or buy** column, select **View details**.
> 4. In the details pane, select **To try or buy, go to Microsoft 365 admin center**. A new tab opens to the Microsoft 365 admin center product page.
> 5. On the **Microsoft Intune Suite** offer page, select **Start free trial**.
> 6. On the **Checkout** page, confirm: **Microsoft Intune Suite Trial**, 90-day term, 250 licenses, **USD 0.00**, no payment method required.
> 7. Select **Edit**, fill the organization profile form with the following information, then select **Save**:
> - **First name**: MOD
> - **Last name**: Administrator1
> - **Address line 1**: 1 Microsoft Way
> - **City**: Redmond
> - **State**: Washington
> - **ZIP**: 98052
> - **Phone**: 425-555-1234
> - **Email address**: admin@<TenantPrefix>.onmicrosoft.com
> 8. Select **Try Now** to activate the trial.
> 9. Return to the Intune admin center. Refresh **Tenant administration → Intune add-ons**. Select the **Your add-ons** tab — within a few minutes you should see **Microsoft Intune Suite Trial** listed with a **Purchased quantity** of **250**. The Suite includes: **Intune Plan 2**, **Remote Help**, **Endpoint Privilege Management**, **Enterprise App Management**, **Advanced Analytics**, and **Cloud PKI**.
>
> **Don't be misled by the All add-ons tab.** The **Microsoft Intune Suite** row will show **"~90 days left in trial"** in the Subscription status column, but the individual capability rows (Intune Plan 2, Endpoint Privilege Management, Remote Help, Enterprise App Management, Advanced Analytics, Cloud PKI) will continue to show **"Available for trial or purchase"**. That's expected — those are the *standalone* add-on SKUs; the Suite trial bundles all of them at the Suite level. Confirm that the Microsoft Intune Suite trial is active by verifying that the Subscription status column displays approximately 89–90 days left in trial.
>
> The trial runs for 90 days, followed by a 30-day grace period. **You can only start the trial once per tenant**, so plan to complete Labs 02–06 inside that window. If the trial is already active, you'll see **Active** in the Subscription status column and can skip the steps above.

---

## Exercise 1: Configure users and groups

### Scenario

Contoso has 33 existing users across multiple departments (Marketing, Legal, IT, Sales, HR, Operations, Engineering, etc.). You'll verify these users, create additional test users for lab scenarios, and configure dynamic groups to enable policy targeting by department and device type.

### Task 1: Review existing users and licenses

1. On **SEA-DEV1**, open **Microsoft Edge**.

1. Navigate to **https://admin.cloud.microsoft.com**.

1. Sign in with the **Global Administrator** account:
   - **Username:** `admin@<TenantPrefix>.onmicrosoft.com`
   - **Password:** (provided by your lab environment)

1. If prompted to stay signed in, select **No** and approve the MFA prompt on your mobile device.

1. In the left navigation, expand **Users** and select **Active users**.

1. Review the list of users. You should see approximately **33 licensed active users** including:
   - Megan Bowen (Marketing Manager)
   - Alex Wilber (Marketing Assistant)
   - Joni Sherman (Paralegal, Legal)
   - Allan Deyoung (IT Admin)
   - Adele Vance (Retail Manager)
   - And others across various departments

   > [!NOTE]
   > The list may also contain unlicensed service accounts (for example, Automate Bot, Conf Room). To see only the 33 licensed users, change the view filter from **All users** to **Licensed users** above the list. These users are pre-provisioned in the Contoso tenant and have Microsoft 365 E5 licenses assigned. You'll use these existing users for policy targeting throughout the labs.

1. Select **Megan Bowen** from the list.

1. In the **Megan Bowen** user details pane, select the **Licenses and apps** tab.

1. Verify that the following licenses are assigned:
   - **Microsoft 365 E5 (no Teams)**
   - **Microsoft Teams Enterprise**

1. Close the user details pane.

**You have successfully reviewed the existing users and verified licensing.**

---

### Task 2: Create test users for additional scenarios

While Contoso has 33 existing users, you'll create two additional test users for specific lab scenarios.

1. In the **Microsoft 365 admin center**, on the **Active users** page, select **Add a user** from the top toolbar.

1. In the **Set up the basics** page, enter the following:
   - **First name:** `Lab`
   - **Last name:** `User1`
   - **Display name:** `Lab User1`
   - **Username:** `LabUser1`
   - **Domains:** Select `<TenantPrefix>.onmicrosoft.com`
   - **Password:** Uncheck **Automatically create a password**, then enter a strong password, such as the pre-provided `<UserPassword>`, in the password field (or use a secure password of your choice).
   - **Require this user to change their password when they first sign in:** Uncheck this box

1. Select **Next**.

1. On the **Assign product licenses** page, leave both licenses **unchecked** and select **Create user without product license**, then select **Next**.

   > [!NOTE]
   > Lab User1 and Lab User2 don't need a license. They exist only to (1) populate `sg-Intune-Pilot-Users` in Task 3 and (2) receive a scoped Intune Administrator role in Exercise 2 Task 5 — neither use touches a licensed workload (Teams, Exchange, Intune device enrollment). Skipping the license also avoids a real capacity problem: the Contoso lab tenant's trial SKUs are fully consumed by the 33 existing users (**Microsoft 365 E5 (no Teams): 20/20 assigned**, **Microsoft Teams Enterprise: 20/20 assigned**), so there are no seats left to give a new user anyway.

1. On the **Optional settings** page, expand **Profile info**.

1. Set the following:
   - **Job title:** `Test User`
   - **Department:** `IT`

1. Select **Next**.

1. On the **Review and finish** page, review the settings and select **Finish adding**.

1. Select **Close** on the confirmation page.

1. Repeat steps 1–10 to create a second test user:
   - **First name:** `Lab`
   - **Last name:** `User2`
   - **Display name:** `Lab User2`
   - **Username:** `LabUser2`
   - **Domains:** Select `<TenantPrefix>.onmicrosoft.com`
   - **Password:** Uncheck **Automatically create a password**, then enter a strong password, such as the pre-provided `<UserPassword>`, in the password field (or use a secure password of your choice).
   - **Job title:** `Test User`
   - **Department:** `Engineering`
   - **Licenses:** Leave unassigned (same reason as Lab User1)

**You have successfully created two additional test users.**

---

### Task 3: Create an assigned security group

You'll create an assigned (static membership) security group for Intune policy targeting.

> [!NOTE]
> If `sg-Intune-Pilot-Users` already exists from a prior lab run, you'll see a name-collision error when you try to create it. In that case, skip the creation steps and jump to step 9 to add members to the existing group.

1. In the **Microsoft 365 admin center**, in the left navigation, expand **Teams & groups** and select **Active teams & groups**.

1. Select the **Security groups** tab.

1. Select **Add a security group**.

1. On the **Set up the basics** page, enter the following:
   - **Name:** `sg-Intune-Pilot-Users`
   - **Description:** `Pilot users for Intune policy testing`

1. Select **Next**.

1. On the **Edit settings** page, leave the default settings and select **Next**.

1. On the **Review and finish adding group** page, select **Create group**.

1. Select **Close** on the confirmation page.

1. On the **Security groups** tab, select **sg-Intune-Pilot-Users** from the list.

1. In the group details pane, select the **Members** tab.

1. Select **View all and manage members**.

1. Select **Add members**.

1. Search for and select the following users:
   - **Megan Bowen**
   - **Alex Wilber**
   - **Joni Sherman**
   - **Lab User1**
   - **Lab User2**

1. Select **Add (5)**.

1. Close the group details pane.

**You have successfully created an assigned security group with five pilot users.**

---

### Task 4: Create a dynamic user group with a compound rule

Dynamic groups automatically update membership based on user attributes. For the Pharmacy clinical workload, you'll create a dynamic group that uses a **compound rule** — combining two conditions with `-and` — to target users in the Pharmacy department who are also located in the US. Compound rules are the canonical pattern for regulatory and per-region scoping (for example, Contoso Healthcare applies stricter compliance to US clinical workloads).

1. In the browser, navigate to **https://entra.microsoft.com**.

1. In the **Microsoft Entra admin center**, select **Groups** in the left navigation, and then select **All groups**.

1. Select **New group** from the top toolbar.

1. In the **New Group** pane, configure the following:
   - **Group type:** Security
   - **Group name:** `dyn-Pharmacy-Users`
   - **Group description:** `Dynamic group for Pharmacy department users located in the US`
   - **Microsoft Entra roles can be assigned to the group:** No
   - **Membership type:** Dynamic User

1. Under **Dynamic user members**, select **Add dynamic query**.

1. On the **Dynamic membership rules** page, on the **Configure Rules** tab, locate the **Rule syntax** box at the bottom of the page and select **Edit** to its right. Authoring the rule directly in the syntax editor is easier to read for compound rules than the property/operator/value builder above it.

1. In the **Edit rule syntax** editor, enter the following compound rule exactly:

   ```text
   (user.department -eq "Pharmacy") -and (user.country -eq "US")
   ```

   > [!NOTE]
   > The `-and` operator means **both** conditions must be true for a user to be included. You can also use `-or` to include users matching either condition, and group sub-expressions in parentheses for more complex logic. The Rule syntax editor validates the expression — fix any red underlines before saving. You may also see a preview banner about the `MemberOf` operator; you can dismiss it because this rule uses `-eq`, not `MemberOf`.

1. Select **OK** to close the editor, then select **Save** at the top of the page.

1. Back in the **New Group** page, select **Create**.

1. After the group is created, select **dyn-Pharmacy-Users** from the groups list.

1. On the group's **Overview** page, in the **Feed** section, locate the **Dynamic rules processing status** card and verify it shows **Succeeded**.

   > [!NOTE]
   > Dynamic group membership evaluation can take 5–15 minutes. Once complete, the group will contain only users whose `department` attribute equals `Pharmacy` **and** whose `country` attribute equals `US`. If no Contoso sample users currently match both attributes, the group will be empty — that's expected for this lab tenant and doesn't affect later exercises.

1. Select the **Members** tab to view group members.

**You have successfully created a dynamic user group with a compound membership rule.**

---

### Task 5: Create a dynamic device group

You'll create a dynamic group that automatically includes all Windows devices enrolled in Intune.

1. In the **Microsoft Entra admin center**, on the **All groups** page, select **New group**.

1. In the **New Group** page, configure the following:
   - **Group type:** Security
   - **Group name:** `dyn-Windows-Devices`
   - **Group description:** `Dynamic group for all Windows devices`
   - **Membership type:** Dynamic Device

1. Under **Dynamic device members**, select **Add dynamic query**.

1. In the **Dynamic membership rules** page, configure the following rule:
   - **Property:** deviceOSType
   - **Operator:** Equals
   - **Value:** `Windows`

1. Select **Save**.

1. Back in the **New Group** page, select **Create**.

   > [!NOTE]
   > This group will automatically populate with Windows devices after they are enrolled in Intune (Exercise 5).

**You have successfully created a dynamic device group for Windows devices.**

---

### Task 6: Create a dynamic device group for Windows Autopilot

You'll create a second dynamic device group, this one for Windows Autopilot registration. You'll use it in **Exercise 6** when you register SEA-DEV3 for Autopilot and assign it a deployment profile.

1. In the **Microsoft Entra admin center**, on the **All groups** page, select **New group**.

1. In the **New Group** page, configure the following:
   - **Group type:** Security
   - **Group name:** `dyn-Autopilot-Devices`
   - **Group description:** `Dynamic group for all Windows Autopilot-registered devices`
   - **Membership type:** Dynamic Device

1. Under **Dynamic device members**, select **Add dynamic query**.

1. On the **Dynamic membership rules** page, on the **Configure Rules** tab, locate the **Rule syntax** box at the bottom of the page and select **Edit** to its right. In the **Edit rule syntax** editor, enter the following rule exactly, then select **OK**:

   ```text
   (device.devicePhysicalIds -any _ -startsWith "[ZTDId]")
   ```

1. Select **Save**, then back in the **New Group** page, select **Create**.

   > [!NOTE]
   > `[ZTDId]` (Zero Touch Deployment ID) is set on a device's directory object as soon as its hardware hash is registered with Windows Autopilot — well before the device goes through OOBE. Unlike `dyn-Windows-Devices` (which only matches devices that have already enrolled), this rule lets you target a device the moment it's registered, which is exactly what an Autopilot deployment profile assignment needs.

**You have successfully created a dynamic device group for Windows Autopilot.**

---

## Exercise 2: Configure administrative delegation

### Scenario

You need to delegate administrative access to team members who will manage different aspects of Intune and device management. You'll use Microsoft Entra ID roles and administrative units to scope permissions appropriately.

### Task 1: Assign the Intune Administrator role

1. In the **Microsoft Entra admin center**, in the left navigation under **Entra ID**, select **Users**, then select **All users**.

1. Search for and select **Allan Deyoung** from the user list.

1. In Allan Deyoung's user details, select **Assigned roles** from the left navigation.

   > [!NOTE]
   > In some Contoso lab tenants, Allan Deyoung is pre-assigned the **Global Administrator** role (visible on the **Active assignments** tab). Adding the Intune Administrator role on top of Global Administrator is functionally redundant — Global Administrator already inherits all Intune permissions. Perform the steps anyway to practice the role-assignment workflow.

1. Select **Add assignments** from the top toolbar.

1. In the **Add assignments** page, on the **Membership** tab, search for and select **Intune Administrator**.

1. Select the **Setting** tab and configure the following:
   - **Assignment type:** **Active** (not **Eligible** — Eligible would require Allan Deyoung to manually activate the role later through PIM before he could use it; Active grants the permissions immediately)
   - **Permanently eligible / Permanently assigned:** Leave checked
   - **Assignment starts:** Leave the auto-populated current date and time
   - **Assignment ends:** Leave blank (greyed out while the permanent checkbox is checked)

1. In the **Justification** box, enter a reason (for example: `Lab 01 role delegation exercise — assigning Intune Administrator to the IT admin`). PIM requires a justification for every Active assignment, even permanent ones.

1. Select **Assign**.

   > [!NOTE]
   > The **Membership**/**Setting** two-tab flow appears because the Contoso lab tenant has Microsoft Entra ID P2 and Privileged Identity Management (PIM) enabled — every directory role assignment goes through PIM by default. **Active** + **Permanently assigned** replicates a classic, always-on role assignment.

   > [!NOTE]
   > The Intune Administrator role grants permissions to manage all aspects of Microsoft Intune, including device configuration, compliance policies, applications, and enrollment settings. This is a less privileged role than Global Administrator.

   > [!NOTE]
   > **This lab uses permanent Active assignments, not PIM's just-in-time (Eligible) model, and that's a deliberate simplification, not the recommended production pattern.** Microsoft's guidance — and this course's own unit content ([Assign Microsoft Entra roles for device management](../Learning%20Path%201%20-%20Prepare%20infrastructure%20for%20devices%20using%20Microsoft%20Intune%20and%20Microsoft%20Entra%20ID/configure-entraid-device-management/includes/04-assign-entra-id-roles-device-management.md)) — recommends **Eligible** assignments for sensitive roles, where the admin activates the role only when needed and the activation expires automatically. We use **Active** here purely so Allan, Joni, and Lab User1 have working permissions for the rest of this lab series without an extra activation step every time. **No lab in this series has learners perform an Eligible-role self-activation** (request access → provide justification → time-boxed activation) — that workflow is covered conceptually in the unit content only. The closest hands-on tie-in is **Lab 06 Exercise 5** (LP6 Unit 05), which has you review PIM activation audit logs, not perform an activation.

**You have successfully assigned the Intune Administrator role to Allan Deyoung.**

---

### Task 2: Assign the Cloud Device Administrator role

1. In the **Microsoft Entra admin center**, under **Entra ID** > **Users** > **All users**, search for and select **Joni Sherman**.

1. In Joni Sherman's user details, select **Assigned roles**.

1. Select **Add assignments**.

1. In the **Add assignments** page, on the **Membership** tab, search for and select **Cloud Device Administrator**.

1. Select the **Setting** tab and configure the same way as Task 1:
   - **Assignment type:** Active
   - **Permanently eligible / Permanently assigned:** Leave checked
   - **Assignment starts / ends:** Leave the defaults (auto-populated start, no end date)

1. In the **Justification** box, enter a reason (for example: `Lab 01 role delegation exercise — assigning Cloud Device Administrator to help desk staff`).

1. Select **Assign**.

   > [!NOTE]
   > The Cloud Device Administrator role allows managing device identities in Microsoft Entra ID, including enabling, disabling, and deleting devices. This role is useful for help desk staff who need to manage device objects without full Intune access.

**You have successfully assigned the Cloud Device Administrator role to Joni Sherman.**

---

### Task 3: Create an administrative unit

Administrative units allow you to restrict administrative permissions to a subset of users or devices. You'll create an administrative unit for the IT department.

1. In the **Microsoft Entra admin center**, in the left navigation under **Entra ID**, select **Roles & admins**, then select **Admin units**.

1. Select **Add** from the top toolbar.

1. In the **Add administrative unit** page, enter the following:
   - **Name:** `IT Department`
   - **Description:** `Administrative unit for IT department users and devices`

1. Select **Next: Assign roles**.

1. On the **Assign roles** page, select **Next: Review + create** (we'll assign roles after adding members).

1. On the **Review + create** page, select **Create**.

**You have successfully created an administrative unit for the IT department.**

---

### Task 4: Add members to the administrative unit

1. On the **Admin units** page, select **IT Department** from the list.

1. In the **IT Department** administrative unit details, select **Users** from the left navigation.

1. Select **Add member** from the top toolbar.

1. Search for and select **Allan Deyoung** (IT Admin).

1. Select **Select**.

1. In the **IT Department** administrative unit details, select **Groups** from the left navigation.

1. Select **Add** from the top toolbar.

1. Search for and select the existing **sg-IT** security group (pre-existing group for IT department users).

1. Select **Select**.

   > [!NOTE]
   > By adding users and groups to the administrative unit, you can scope administrative roles to only manage these objects. This is useful for delegating regional or departmental administration.

**You have successfully added members to the IT Department administrative unit.**

---

### Task 5: Assign a scoped role to the administrative unit

You'll assign a Helpdesk Administrator role scoped to only the IT Department administrative unit.

> [!NOTE]
> **Intune Administrator can't be assigned with administrative unit scope.** Only a fixed set of Microsoft Entra roles support AU scoping — Authentication Administrator, Attribute Assignment Administrator/Reader, Cloud Device Administrator, Groups Administrator, **Helpdesk Administrator**, License Administrator, Password Administrator, Printer Administrator, Privileged Authentication Administrator, SharePoint Administrator, Teams Administrator, Teams Devices Administrator, User Administrator, and any custom role — Intune Administrator isn't one of them. This is exactly why Intune has its own separate scope-tag system (Task 6): that's the supported way to delegate Intune-specific administration to a subset of devices/policies. Helpdesk Administrator is Microsoft's own canonical example for AU-scoped delegation, so we'll use it here to demonstrate the Entra-layer scoping mechanic.

1. In the **IT Department** administrative unit details, select **Roles and administrators** from the left navigation.

1. On the list of roles, search for and select **Helpdesk Administrator** by clicking its name (this page only lists roles that support administrative unit scope — there's no toolbar **Add** button that lets you search for an arbitrary role; you pick from the list shown).

1. On the role's assignment page, select **Add assignments**.

1. In the **Add assignments** page, on the **Membership** tab, select **No member selected**, then search for and select **Lab User1** (created in Exercise 1).

1. Select the **Setting** tab and configure:
   - **Assignment type:** Active
   - **Permanently eligible / Permanently assigned:** Leave checked
   - **Assignment starts / ends:** Leave the defaults

1. In the **Justification** box, enter a reason (for example: `Lab 01 role delegation exercise — scoped Helpdesk Administrator for IT Department AU`).

1. Select **Assign**.

   > [!NOTE]
   > Lab User1 now has Helpdesk Administrator permissions, but only for users and devices within the IT Department administrative unit. This demonstrates role-based access control (RBAC) scoping at the Microsoft Entra layer.

**You have successfully assigned a scoped Helpdesk Administrator role.**

---

### Task 6: Create a custom Intune role and scope tag for the Pharmacy clinical workload

Microsoft Entra ID roles (Task 1–5) delegate Entra-level permissions. Intune itself has a **separate RBAC system** with its own custom roles and **scope tags**. Contoso Healthcare wants the Pharmacy helpdesk to see and act on Pharmacy clinical devices only — not the whole tenant — so you'll create a `Pharmacy` scope tag and a `Pharmacy Helpdesk` custom Intune role now. In **Labs 2–4** you'll apply the `Pharmacy` scope tag to specific configuration, compliance, app, and security policies. In **Lab 05 Exercise 3** you'll assign the `Pharmacy Helpdesk` role to a delegated administrator (Lee Gu) and verify end-to-end that they see only Pharmacy-scoped objects.

**Part A — Create the `Pharmacy` scope tag**

1. In the browser, navigate to **https://intune.microsoft.com** (Microsoft Intune admin center).

1. In the left navigation, select **Tenant administration**, and then select **Roles**.

1. On the **Roles** page, select **Scope (Tags)** (also labeled **Scope tags** in some portal builds).

1. Select **+ Create**.

1. On the **Basics** tab, enter:
   - **Name:** `Pharmacy`
   - **Description:** `Pharmacy clinical devices and policies (Contoso Healthcare)`

1. Select **Next**.

1. On the **Assignments** tab, leave **Groups** empty for now — you'll tag specific policies (not groups) starting in **Lab 02 Exercise 1**. Select **Next**.

1. On the **Review + create** tab, select **Create**.

**Part B — Create the `Pharmacy Helpdesk` custom Intune role**

1. In **Tenant administration**, select **Roles**, then select **All roles**.

1. Select **+ Create** → **Intune role**.

1. On the **Basics** page, enter the following:
   - **Name:** `Pharmacy Helpdesk`
   - **Description:** `Delegated helpdesk role scoped to Pharmacy clinical devices. Read + remote actions on devices; no policy authoring.`

1. Select **Next**.

1. On the **Permissions** page, select **Yes** for the following permissions (leave everything else **No** — this is principle of least privilege). Portal labels group permissions into categories like **Managed devices**, **Remote tasks**, **Organization**, and **Roles**. Match the closest available labels in your portal:

   - **Managed devices:** Read, Set primary user, Update
   - **Remote tasks:** Sync devices, Restart now (or Reboot now), Collect diagnostics
   - **Organization:** Read
   - **Roles:** Read
   - **Remote Help app**: Take full control, View screen

   > [!IMPORTANT]
   > Leave **all** permissions on **Apps**, **Device compliance policies**, **Device configurations**, **Endpoint protection**, **Enrollment programs**, and **Policy sets** set to **No**. The Pharmacy Helpdesk should be able to act on devices but **not** author or modify any policy. This is the upper-intermediate delegation pattern: a narrow remote-action role layered on top of broad read.

1. Select **Next**.

1. On the **Scope tags** page, select **+ Select scope tags** and add the **Pharmacy** scope tag you created in Part A. Select **Select**.

1. Remove the **Default** scope tag chip (select the ellipsis **...** → **Remove**) so only **Pharmacy** remains selected.

   > [!NOTE]
   > This step scopes the **role definition itself**, not what the assigned admin can manage — those are two different things. Per Microsoft: *"The scope tag added on a role controls visibility of the role itself. The scope tag added in role assignment limits the visibility of Intune objects, like policies, apps, or devices, to only administrators in that role assignment."* Removing **Default** here keeps the Pharmacy Helpdesk role definition visible only to admins who already have the Pharmacy scope tag (Global/Intune Administrators still see everything — scope tags don't apply to Entra roles). The step that actually restricts what Lee Gu can manage day-to-day happens in **Lab 05 Exercise 3**, when you assign this role with Pharmacy as the assignment's scope.

1. Select **Next**.

1. On the **Review + create** page, select **Create**.

> [!NOTE]
> The `Pharmacy` scope tag and `Pharmacy Helpdesk` role you just created are the foundation for delegated administration across the rest of this lab series. In **Labs 02–04** you'll apply the `Pharmacy` scope tag to configuration profiles, compliance policies, an LOB app, and a security baseline. In **Lab 05 Exercise 3** you'll assign the `Pharmacy Helpdesk` role to a delegated administrator (Lee Gu) and verify they see only Pharmacy-scoped objects. In **Lab 06 Exercise 2** the Pharmacy Helpdesk admin uses Remote Help on Pharmacy devices.

**You have successfully created the `Pharmacy` scope tag and the `Pharmacy Helpdesk` custom Intune role.**

---

## Exercise 3: Configure device registration and settings

### Scenario

Before devices can enroll in Intune, you need to configure device registration settings in Microsoft Entra ID, including who can register devices, device limits, and additional local administrator accounts. You'll also enable Microsoft Entra LAPS for local administrator password management.

### Task 1: Configure device join settings

1. In the **Microsoft Entra admin center**, in the left navigation under **Entra ID**, select **Devices**, then select **Overview**.

1. Select **Device settings** from the left navigation.

1. On the **Device settings** page, under **Microsoft Entra join and registration settings**, configure the following:
   - **Users may join devices to Microsoft Entra:** Select **All** *(options: All / Selected / None)*
   - **Users may register their devices with Microsoft Entra:** Should already show **All**, and the control is **greyed out/non-interactive** — this is expected, not a bug
   - **Require Multifactor Authentication to register or join devices with Microsoft Entra:** Select **No**
   - **Maximum number of devices per user:** `50`

   > [!NOTE]
   > **"Users may register their devices" is greyed out at All** — expected, not a bug. Intune/MDM auto-enrollment is already active in this tenant, and registration is required for MDM enrollment, so Entra locks the toggle. Nothing to configure here.
   >   > You'll see a yellow recommendation banner advising you to require MFA via Conditional Access rather than this toggle. For this lab, leave the MFA toggle set to **No** — Conditional Access enforcement is covered in Lab 04. In a production environment, you would restrict device registration to specific groups and require MFA. For lab purposes, we're allowing all users to register devices without MFA to simplify enrollment.

1. Select **Save** at the top of the page if you made any changes.

**You have successfully configured device join settings.**

---

### Task 2: Configure additional local administrators on Microsoft Entra joined devices

By default, the user who performs a Microsoft Entra join becomes a local administrator on the device. You can add additional users or groups to the local administrators group.

1. On the **Device settings** page, scroll down to the **Local administrator settings** section.

   > [!NOTE]
   > Two preview toggles are visible here — **Global administrator role is added as local administrator on the device during Microsoft Entra join (Preview)** and **Registering user is added as local administrator on the device during Microsoft Entra join (Preview)**. Leave both at their default values for this lab.

1. Select the **Manage Additional local administrators on all Microsoft Entra joined devices** link.

1. On the **Device Administrators | Assignments** page, select **Add assignments**.

1. Search for and select **Allan Deyoung**.

1. Select **Add**.

   > [!NOTE]
   > Allan Deyoung is now added to the local Administrators group on any Microsoft Entra joined device. This is useful for help desk staff who need local admin rights on managed devices. To delegate this via a group instead of individual users, you'd need a dedicated role-assignable group (**Microsoft Entra roles can be assigned to the group: Yes**, set at creation).

**You have successfully configured additional local administrators for Microsoft Entra joined devices.**

---

### Task 3: Enable Microsoft Entra Local Administrator Password Solution (LAPS)

Microsoft Entra LAPS automatically manages and rotates local administrator passwords on Microsoft Entra joined devices.

> [!IMPORTANT]
> Detailed LAPS policy configuration (password complexity, length, age, and managed account name) has moved out of the Entra admin center and into Microsoft Intune as an endpoint security policy. The Entra setting is now a single on/off toggle that enables the LAPS feature for the tenant; the password policy itself is configured in Intune.

**Part A — Enable LAPS at the tenant level (Entra admin center):**

1. In the **Microsoft Entra admin center**, in the left navigation under **Entra ID**, select **Devices**, then select **Device settings**.

1. Scroll down to the **Local administrator settings** section.

1. Set **Enable Microsoft Entra Local Administrator Password Solution (LAPS)** to **Yes**.

1. Select **Save** at the top of the page.

**Part B — Configure the LAPS password policy (Intune admin center):**

1. In the browser, navigate to **https://intune.microsoft.com**.

1. In the **Microsoft Intune admin center**, select **Endpoint security** in the left navigation, and then select **Account protection**.

1. Select **+ Create Policy**.

1. In the **Create a profile** pane, configure the following:
   - **Platform:** Windows
   - **Profile:** Local admin password solution (Windows LAPS)

1. Select **Create**.

1. On the **Basics** tab, enter:
   - **Name:** `Contoso LAPS Policy`
   - **Description:** `Manages and rotates the local Administrator password on Microsoft Entra joined devices`

1. Select **Next**.

1. On the **Configuration settings** tab, configure the following:
   - **Backup Directory:** Backup the password to Microsoft Entra ID only
   - **Password Age Days:** `30`
   - **Administrator Account Name:** Leave as Not configured (uses the built-in Administrator)
   - **Password Complexity:** Large letters + small letters + numbers + special characters (Default)
   - **Password Length:** `14`
   - **Automatic Account Management Enabled:** The target account will not be automatically managed (Default)
   - **Post Authentication Actions:** Reset the password and logoff the managed account...
   - **Post Authentication Reset Delay:** select Configured and enter `24` for hours

   > [!NOTE]
   > **Automatic Account Management** (Windows 11 24H2+ only) lets LAPS create/enable a local admin account itself. Leave it **the target account will not be automatically managed (Default)** here — the lab VMs aren't guaranteed to be on 24H2, and we're already using the existing built-in Administrator account, so it isn't needed. **Post Authentication Actions** options are: *Reset the password* / *Reset the password and logoff the managed account* (the default, and what we're using) / *Reset the password and reboot*.

1. Select **Next**.

1. On the **Scope tags** tab, select **Next**.

1. On the **Assignments** tab, under **Groups**, select **All devices**.

1. Select **Next**.

1. On the **Review + create** tab, review the settings and select **Create**.

   > [!NOTE]
   > Microsoft Entra LAPS automatically rotates the local administrator password every 30 days and stores the password securely in Microsoft Entra ID. Authorized administrators can retrieve the password from the Entra admin center under **Devices** > **Local administrator password recovery**.

**You have successfully enabled Microsoft Entra LAPS and configured the password policy in Intune.**

---

## Exercise 4: Configure Windows enrollment policies

### Scenario

In Exercise 5 your colleagues will sign in to **SEA-DEV1** and **SEA-DEV2** and perform a Microsoft Entra join, and in Exercise 6 you'll register **SEA-DEV3** for Windows Autopilot. Before any of that happens, you need to make sure the tenant is configured so the **first-run experience is right**: devices get automatically enrolled in Intune, the user can't start working until critical apps and policies are in place, and you have guardrails on how many devices each user can enroll.

In this exercise you'll:

- Verify that automatic Intune enrollment is configured correctly for new tenants
- Configure the **Enrollment Status Page (ESP)** so devices block until apps and policies are applied — the same gate that makes Autopilot deployments feel polished
- Create a targeted, stricter ESP profile for the pilot group
- Review the default platform restriction policy and create a device limit restriction policy

> [!NOTE]
> **Why automatic MDM enrollment isn't the focus anymore.** In modern, cloud-only Microsoft 365 tenants, **automatic Intune enrollment is on by default** for the All-users scope. The classic "configure MDM user scope" step is now most relevant in **hybrid identity** and **Configuration Manager co-management** scenarios where you need to scope which on-premises-synced users are auto-enrolled. You'll verify the setting in Task 1, then move on to the policies that actually shape the user's first-run experience.

### Task 1: Verify automatic MDM enrollment

1. In the browser, navigate to **https://intune.microsoft.com**.

1. In the **Microsoft Intune admin center**, select **Devices** in the left navigation.

   > [!NOTE]
   > You may see a one-time **"Devices has changed"** tour banner. Select **Skip** to dismiss it.

1. Under **Device onboarding**, select **Enrollment**.

1. On the **Windows** tab, under **Enrollment options**, select **Automatic Enrollment**.

1. Confirm that **MDM user scope** is set to **All**.

   > [!NOTE]
   > In a brand-new cloud-only tenant, this setting is already configured. If it shows **None**, change it to **All** and select **Save**.

1. Note that **Windows Information Protection (WIP) user scope** is set to **None** and shows the banner: *"Creating new WIP without enrollment policies (WIP-ME) is no longer supported..."* Leave this set to **None** — Windows Information Protection is deprecated. You'll use App Protection Policies (MAM) for mobile data protection in Lab 03.

1. Leave the **MDM terms of use URL**, **MDM discovery URL**, and **MDM compliance URL** at their auto-populated defaults.

1. If you made any change, select **Save**. Otherwise, close the **Automatic Enrollment** pane.

**You have verified that automatic MDM enrollment is configured for your tenant.**

---

### Task 2: Configure the Default Enrollment Status Page

The **Enrollment Status Page (ESP)** is shown to users during Windows enrollment (Microsoft Entra join, Autopilot, or device enrollment). It blocks device use until configured apps and policies are applied, so users don't sign in to a half-provisioned device. The **Default** ESP profile targets all users and all devices and ships disabled — you'll enable it to set a baseline for Contoso.

1. In the **Microsoft Intune admin center**, on the **Enrollment** page, make sure you are on the **Windows** tab. Under **Windows Autopilot**, select **Enrollment Status Page**.

1. On the **Enrollment Status Page** list, select the **All users and all devices** link (assigned with **Default** Priority).

1. On the **All users and all devices** page, select **Manage > Properties** in the left navigation, then select **Edit** next to **Settings**.

1. Configure the following settings:
   - **Show app and profile configuration progress:** Yes
   - **Show an error when installation takes longer than specified number of minutes:** `60`
   - **Show custom message when time limit or error occurs:** Yes
     - **Custom message:** `Contoso device setup is taking longer than expected. Contact the Service Desk at x4040 if this persists.`
   - **Turn on log collection and diagnostics page for end users:** Yes
   - **Only show page to devices provisioned by out-of-box experience (OOBE):** No
   - **Block device use until all apps and profiles are installed:** No

   > [!NOTE]
   > Setting **Block device use until all apps and profiles are installed** to **No** on the Default profile lets standard users sign in quickly while non-blocking policies finish in the background. In Task 3 you'll create a stricter, blocking ESP for the pilot group.

1. Select **Review + save**, then select **Save**.

**You have successfully configured the Default Enrollment Status Page.**

---

### Task 3: Create a blocking ESP profile for the pilot group

Pilot users at Contoso Healthcare receive corporate laptops pre-staged for clinical workflows. You'll create a stricter ESP profile that blocks device use until required apps are installed, and assign it to `sg-Intune-Pilot-Users` so it takes priority over the Default.

1. On the **Enrollment Status Page** list, select **+Create**.

1. On the **Basics** tab, enter:
   - **Name:** `ESP - Pilot - Blocking`
   - **Description:** `Blocks pilot devices from use until clinical apps and security baseline are installed`

1. Select **Next**.

1. On the **Settings** page, configure:
   - **Show app and profile configuration progress:** Yes
   - **Show an error when installation takes longer than specified number of minutes:** `60`
   - **Show custom message when time limit or error occurs:** Yes
     - **Custom message:** `Contoso pilot device setup is in progress. Contact the Service Desk at x4040 if this persists.`
   - **Turn on log collection and diagnostics page for end users:** Yes
   - **Only show page to devices provisioned by out-of-box experience (OOBE):** No
   - **Block device use until all apps and profiles are installed:** Yes
   - **Allow users to reset device if installation error occurs:** Yes
   - **Allow users to use device if installation error occurs:** No
   - **Block device use until required apps are installed if they are assigned to the user/device:** All

1. Select **Next**.

1. On the **Assignments** page, under **Included groups**, select **Add groups**.

1. Search for and select **sg-Intune-Pilot-Users**, then select **Select**.

1. Select **Next**, then **Next** again to skip **Scope tags**.

1. On the **Review + create** tab, select **Create**.

1. Back on the **Enrollment Status Page** list, confirm `ESP - Pilot - Blocking` appears with **Priority 1** (above **Default**). The first profile a user/device matches wins.

   > [!NOTE]
   > ESP profiles are evaluated by priority. Because `ESP - Pilot - Blocking` is assigned to `sg-Intune-Pilot-Users` and sits at higher priority, pilot users will receive the blocking experience while everyone else falls through to **Default**.

**You have successfully created a targeted Enrollment Status Page profile for pilot users.**

---

### Task 4: Review default enrollment restrictions

Enrollment restrictions control which device platforms can enroll in Intune. Reviewing the defaults helps you understand what the Contoso tenant will accept before SEA-DEV1 and SEA-DEV2 enroll in Exercise 5.

1. In the **Microsoft Intune admin center**, on the **Enrollment** page, make sure you are on the **Windows** tab. Under **Enrollment options**, select **Device platform restriction**.

1. On the **Enrollment restrictions** page, under **Device type restrictions**, select the **All Users** link (**Default** priority).

1. Select **Manage > Properties** in the left navigation. Select **Edit** next to **Platform settings**.

1. In the **Default** restriction policy, review the current **Platform settings**. Review which device platforms are allowed (for example, Windows, Android, iOS/iPadOS, and macOS) and the enrollment restrictions configured for each platform, such as Personally owned, Versions, and Device manufacturer settings.

   > [!NOTE]
   > The default policy allows all platforms and personally owned devices. In production you might block personally owned Windows devices or restrict specific OS versions, but for the lab leave the defaults in place so SEA-DEV1 and SEA-DEV2 can enroll in Exercise 5.

1. Close the policy details pane without making changes.

**You have successfully reviewed the default enrollment restrictions.**

---

### Task 5: Create a device limit restriction policy

You'll create a policy that limits how many devices each user can enroll. This protects Contoso from license sprawl and stolen-credential abuse.

1. In the **Microsoft Intune admin center**, on the **Enrollment** page (**Devices** > **Device onboarding** > **Enrollment**), make sure you are on the **Windows** tab. Under **Enrollment options**, select **Device limit restriction**.

1. Select **Create restriction**.

1. In the **Create restriction** page, enter the following and select **Next**:
   - **Name:** `Device Limit - 10 Devices`
   - **Description:** `Limit users to 10 enrolled devices`

1. Under **Device limit**, enter `10` and select **Next**.

1. Select **Next** and skip **Scope tags**.

1. Under **Assignments**, select **Add groups**.

1. Search for and select **sg-Intune-Pilot-Users**.

1. Select **Select**.

1. Select **Next**.

1. Under **Review + create**, select **Create**.

   > [!NOTE]
   > This policy limits all users to 10 enrolled devices. When a user reaches the limit, they must unenroll an existing device before enrolling a new one.

**You have successfully created and assigned a device limit restriction policy.**

---

### Task 6: Block personally owned Android devices

Contoso Healthcare doesn't want personal Android phones enrolling in Intune — only corporate-owned Android Enterprise devices (Samsung Knox / corporate-issued) are permitted, primarily because clinical data handling rules at Contoso require corporate ownership for any device that touches the network. You'll create a **Device platform restriction** that blocks personally owned Android enrollment while leaving corporate Android Enterprise allowed.

1. In the **Microsoft Intune admin center**, on the **Enrollment** page (**Devices** > **Device onboarding** > **Enrollment**), select the **Android** tab.

   > [!NOTE]
   > Platform restrictions are configured per platform. The **Default** Android platform restriction allows all Android subtypes (personal work profile, corporate-owned work profile, fully managed, dedicated). You'll create a higher-priority custom restriction that blocks the personally owned subtypes.

1. Under **Enrollment options**, select **Device platform restriction**.

1. Select **Android restriction → + Create restriction**.

1. On the **Basics** tab, enter:
   - **Name:** `Android - Block personal`
   - **Description:** `Block personally owned Android enrollment; allow corporate-owned Android Enterprise only`

1. Select **Next**.

1. On the **Platform settings** tab, you'll see a table with two rows — **Android Enterprise (work profile)** and **Android device administrator** — each with its own **Platform** (Allow/Block) and **Personally owned** (Allow/Block) toggle, plus optional version range and device manufacturer filters. There's no separate row or toggle for "corporate-owned"; ownership is set per-row via **Personally owned**. Leaving **Platform** set to **Allow** while **Personally owned** is set to **Block** means that the row still allows the type when it's corporate-owned.

   Configure:
   - **Android Enterprise (work profile) → Platform:** Allow
   - **Android Enterprise (work profile) → Personally owned:** Block
   - **Android device administrator → Platform:** Block (legacy DA enrollment is end-of-life — you'll also see a banner noting Intune ended support for Android device administrator management on GMS devices as of December 31, 2024)
   - **Android device administrator → Personally owned:** Block (greyed out since the row is already blocked)

   Leave version range and device manufacturer blank on both rows.

   > [!NOTE]
   > Net effect: personally owned Android Enterprise work-profile (BYOD) devices are blocked; corporate-owned Android Enterprise work-profile devices are allowed (Platform = Allow covers them since only the personal subset is blocked); Android device administrator is blocked outright regardless of ownership.

1. Select **Next**.

1. On the **Scope tags** tab, leave the **default** scope tag (this restriction is tenant-wide, not Pharmacy-scoped). Select **Next**.

1. On the **Assignments** tab, under **Included groups**, select **Add groups**, search and select **sg-Intune-Pilot-Users**, and then select **Next**.

1. On the **Review + create** tab, select **Create**.

1. On the **Enrollment restrictions** page, confirm `Android - Block personal` appears in the list with priority **1** (above **Default**). Higher-priority restrictions evaluate first.

   > [!NOTE]
   > In production, you'd typically do this for every platform you don't manage (block personal iOS, block Linux, etc.). The Pharmacy clinical workload at Contoso explicitly forbids personal devices on the network because Contoso can't enforce encryption, jailbreak detection, or app-protection baselines on devices it doesn't own.

**You have successfully blocked personally owned Android device enrollment.**

---

## Exercise 5: Enroll Windows devices

### Scenario

You'll now enroll two Windows 11 devices (SEA-DEV1 and SEA-DEV2) into Intune by performing a Microsoft Entra join. This simulates a user-driven enrollment scenario where an employee joins their device to the corporate tenant.

### Task 1: Perform a Microsoft Entra join and enrollment on SEA-DEV1

1. On **SEA-DEV1**, sign out of the current session if signed in.

1. At the Windows sign-in screen, select **Admin** from the account list in the lower-left corner. (If **Admin** isn't listed, select **Other user** and enter the username `Admin`.)

1. Sign in with the local administrator account:
   - **Username:** `Admin`
   - **Password:** (provided by your lab environment)

1. After signing in, open **Settings** (press `Windows + I`).

1. Navigate to **Accounts** → **Access work or school**.

1. Select **Connect**.

1. In the **Set up a work or school account** dialog, select **Join this device to Microsoft Entra ID**.

1. On the **Sign in** dialog, enter the following and select **Next**:
   - **Email address:** `MeganB@<TenantPrefix>.OnMicrosoft.com`

1. On the **Enter password** dialog, enter Megan Bowen's password and select **Sign in**.

1. On the **Make sure this is your organization** dialog, verify the tenant is **<TenantPrefix>.onmicrosoft.com** and select **Join**.

1. On the **You're all set!** page, select **Done**.

   > [!NOTE]
   > The device is now Microsoft Entra joined and automatically enrolled in Intune. Megan sees the Enrollment Status Page you configured in Exercise 4 while apps and policies are applied. Because Megan isn't in the `sg-Intune-Pilot-Users` group, she gets the non-blocking **Default** profile rather than the stricter **ESP - Pilot - Blocking** profile.

**You have successfully enrolled SEA-DEV1 in Microsoft Entra and Intune.**

---

### Task 2: Verify SEA-DEV1 enrollment in the Intune admin center

1. On **SEA-DEV1**, open **Microsoft Edge** and navigate to **https://intune.microsoft.com**.

1. Sign in as **admin@<TenantPrefix>.onmicrosoft.com** (if not already signed in).

1. In the **Microsoft Intune admin center**, select **Devices**, and then select **All devices**.

1. Verify that **SEA-DEV1** appears in the device list with:
   - **Managed by:** Intune
   - **Ownership:** Corporate
   - **Compliance:** Compliant (may show "Not evaluated" initially)

1. Select **SEA-DEV1** from the list to view device details.

1. Review the following tabs:
   - **Overview:** Device name, operating system, compliance status, and last check-in time.
   - **Hardware:** Serial number, TPM version, total storage space
   - **Discovered apps:** (will populate over time as app inventory syncs)

1. Tag this device as a Pharmacy clinical device so the delegated **Pharmacy Helpdesk** admin can see and act on it in later labs. On the **SEA-DEV1** device page, under **Manage**, select **Properties**.

1. Next to **Scope tags**, select **Open** to open the **Select tags** pane.

1. In the **Select tags** pane, select **Pharmacy** (the scope tag you created in **Exercise 2 Task 6**), then select **Select**.

1. Select **Save**.

**You have successfully verified SEA-DEV1 enrollment in Intune.**

---

### Task 3: Perform a Microsoft Entra join and enrollment on SEA-DEV2

1. Switch to **SEA-DEV2**.

1. Sign in with the local administrator account:
   - **Username:** `Admin`
   - **Password:** (provided by your lab environment)

1. Open **Settings** (`Windows + I`).

1. Navigate to **Accounts** → **Access work or school**.

1. Select **Connect**.

1. In the **Set up a work or school account** dialog, select **Join this device to Microsoft Entra ID**.

1. On the **Sign in** dialog, enter:
   - **Email address:** `JoniS@<TenantPrefix>.OnMicrosoft.com`
   - Select **Next**

1. On the **Enter password** dialog, enter Joni Sherman's password and select **Sign in**.

1. On the **Make sure this is your organization** dialog, select **Join**.

1. On the **You're all set!** dialog, select **Done**.

1. Restart **SEA-DEV2**.

1. After restart, sign out and sign in as:
   - **User:** `JoniS@<TenantPrefix>.OnMicrosoft.com`
   - **Password:** (Joni Sherman's password)

**You have successfully enrolled SEA-DEV2 in Microsoft Entra and Intune.**

---

### Task 4: Verify both devices are enrolled

1. Switch to **SEA-DEV1**. On **SEA-DEV1**, in the **Microsoft Intune admin center**, navigate to **Devices** → **All devices**.

1. Verify both **SEA-DEV1** and **SEA-DEV2** appear in the device list.

1. Verify the **dyn-Windows-Devices** dynamic group now contains both devices:
   - In the **Microsoft Intune admin center**, navigate to **Groups** → **All groups**.
   - Select **dyn-Windows-Devices**.
   - Select the **Members** tab.
   - Verify **SEA-DEV1** and **SEA-DEV2** are listed (may take 5–10 minutes for dynamic group membership to update).

**You have successfully verified both devices are enrolled and automatically added to the dynamic device group.**

---

## Exercise 6: Configure Windows Autopilot

### Scenario

Windows Autopilot streamlines device provisioning by automatically joining devices to Microsoft Entra ID and enrolling them in Intune during the out-of-box experience (OOBE). You'll register SEA-DEV3 for Autopilot, create a deployment profile, and assign it to the device.

> [!NOTE]
> Due to lab time constraints, you will not perform a full Autopilot OOBE (which requires resetting the device). You'll complete the registration and configuration steps to understand the Autopilot deployment workflow.

> [!NOTE]
> **This is classic Autopilot (hardware-hash based), not Windows Autopilot device preparation.** Device preparation is a newer, simpler re-architecture that skips manual hash registration entirely for its supported scenarios (user-driven, physical devices) — devices just enroll and get added to a security group at enrollment time. But it doesn't yet support pre-provisioned, self-deploying, existing-devices, hybrid join, or Autopilot Reset scenarios — those still require classic Autopilot. Manual hardware-hash registration (what you're doing here) is Microsoft's own documented approach for **testing and evaluation**, which is exactly this lab's context; production registration normally happens automatically via the OEM/reseller/CSP instead.

### Task 1: Generate the Autopilot hardware hash for SEA-DEV3

The Autopilot hardware hash uniquely identifies a device and is required for Autopilot registration.

1. Switch to **SEA-DEV3**.

1. Sign in with the local administrator account:
   - **Username:** `Admin`
   - **Password:** (provided by your lab environment)

1. Right-click the **Start** button and select **Terminal (Admin)**. On Windows 11, the Power User menu lists Windows Terminal, which opens a PowerShell tab by default.

1. In the **Do you want to allow this app to make changes to your device?** dialog, select **Yes**.

1. In the PowerShell session, create a folder for the output file and install the **Get-WindowsAutopilotInfo** script (this is a PowerShell Gallery **script**, not a module):

   ```powershell
   New-Item -ItemType Directory -Path C:\Autopilot -Force
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
   Install-Script -Name Get-WindowsAutopilotInfo -Force
   ```

1. After installation completes, generate the Autopilot hardware hash and export it to a CSV file:

   ```powershell
   Get-WindowsAutopilotInfo -OutputFile C:\Autopilot\SEA-DEV3-AutopilotHash.csv
   ```

1. Verify the CSV file was created:

   ```powershell
   Test-Path C:\Autopilot\SEA-DEV3-AutopilotHash.csv
   ```

   The output should return **True**.

1. Open the CSV file to verify the hardware hash was captured:

   ```powershell
   notepad C:\Autopilot\SEA-DEV3-AutopilotHash.csv
   ```

1. Review the CSV contents. It should contain:
   - **Device Serial Number**
   - **Windows Product ID**
   - **Hardware Hash** (long base64-encoded string)

1. Close Notepad.

**You have successfully generated the Autopilot hardware hash for SEA-DEV3.**

---

### Task 2: Upload the hardware hash to Intune

1. Switch to **SEA-DEV1**.

1. In **Microsoft Edge**, navigate to **https://intune.microsoft.com** (sign in as admin if needed).

1. In the **Microsoft Intune admin center**, select **Devices**, and under **Device onboarding**, select **Enrollment**.

1. Under **Windows Autopilot**, select **Devices**.

1. Select **Import** from the top toolbar.

1. In the **Add Autopilot devices** pane, select the folder icon to browse for the CSV file.

1. Navigate to **\\\SEA-DEV3\C$\Autopilot\\** (or copy the CSV file from SEA-DEV3 to SEA-DEV1 using a shared folder or USB).

   > [!NOTE]
   > If you cannot access SEA-DEV3's file system from SEA-DEV1, manually copy the CSV file to SEA-DEV1 (e.g., save to a USB drive, or use the lab platform's file transfer mechanism).

1. Select **SEA-DEV3-AutopilotHash.csv** and select **Open**.

1. In the **Add Autopilot devices** pane, select **Import**.

1. Wait for the import to complete. A notification will appear when the import finishes (typically 1–2 minutes).

1. After import completes, refresh the **Devices** page. You should see **SEA-DEV3** appear in the Autopilot devices list.

   > [!NOTE]
   > It may take 5–10 minutes for the device to fully sync and appear in the list. If the device doesn't appear immediately, refresh the page periodically.

**You have successfully uploaded the SEA-DEV3 hardware hash to Intune.**

---

### Task 3: Create a Windows Autopilot deployment profile

Autopilot deployment profiles define the OOBE experience and determine which settings users can configure during setup.

1. In the **Microsoft Intune admin center**, on the **Device | Enrollment** page, select **Deployment Profiles** (under Windows Autopilot).

1. Select **Create profile** → **Windows PC**.

1. On the **Basics** tab, enter:
   - **Name:** `Autopilot User Driven Profile`
   - **Description:** `User driven Microsoft Entra join profile for Windows Autopilot`
   - **Convert all targeted devices to Autopilot:** No

1. Select **Next**.

1. On the **Out-of-box experience (OOBE)** tab, configure the following:
   - **Deployment mode:** User-driven
   - **Join to Microsoft Entra ID as:** Microsoft Entra joined
   - **Microsoft Software License Terms:** Hide
   - **Privacy Settings:** Hide
   - **Hide change account options:** Hide
   - **User account type:** Standard
   - **Allow pre-provisioned deployment:** No
   - **Apply device name template:** No

   > [!NOTE]
   > This configuration simplifies the OOBE by hiding unnecessary prompts. Users will sign in with their Microsoft Entra credentials, and the device will be automatically configured.

1. Select **Next** and **Next** again to skip **Scope tags**.

1. On the **Assignments** tab, under **Include groups**, select **Add groups**.

1. Search for and select **dyn-Autopilot-Devices**.

1. Select **Select**.

   > [!NOTE]
   > By assigning the profile to `dyn-Autopilot-Devices`, any device registered in Autopilot — enrolled or not — automatically receives this deployment profile, which is what actually lets SEA-DEV3's Profile status reach **Assigned** in Task 4.

1. Select **Next**.

1. On the **Review + create** tab, review the settings and select **Create**.

**You have successfully created a Windows Autopilot deployment profile.**

---

### Task 4: Review the Autopilot profile status for SEA-DEV3

1. In the **Microsoft Intune admin center**, navigate to **Devices** → **Enrollment** → **Devices** (under Windows Autopilot).

1. Select **SEA-DEV3** from the Autopilot devices list.

1. Review the device details:
   - **Profile status:** Should now show **Assigned** (it may take a few minutes for the dynamic group to populate and the profile assignment to sync)
   - **Group tag:** None
   - **User:** unassigned 

   > [!NOTE]
   > If it still shows "Not assigned" after several minutes, select **Sync** from the toolbar on the **Devices** list to force a sync. Also double check `dyn-Autopilot-Devices` actually shows SEA-DEV3 as a member (**Groups** → `dyn-Autopilot-Devices` → **Members**) — if SEA-DEV3 isn't there, re-check the rule syntax from Task 3.

1. Close the device properties pane.

**You have successfully assigned the Autopilot deployment profile to SEA-DEV3.**

---

### Task 5: (Optional) Understand the Autopilot OOBE flow

In a production environment, the next step would be to reset SEA-DEV3 and go through the Autopilot OOBE. Here's what would happen:

1. **Device boots:** SEA-DEV3 is powered on (factory-reset or new device).

1. **Autopilot recognition:** During OOBE, Windows contacts the Autopilot service and recognizes the device by its hardware hash.

1. **Profile download:** The device downloads the assigned Autopilot profile (`Autopilot User-Driven Profile`).

1. **Simplified OOBE:** The user sees a simplified OOBE with Microsoft branding:
   - No license terms or privacy prompts (hidden per profile settings)
   - User signs in with Microsoft Entra credentials (e.g., `AlexW@<TenantPrefix>.OnMicrosoft.com`)
   - Device automatically joins Microsoft Entra ID and enrolls in Intune

1. **Policy application:** After enrollment, Intune policies (configuration profiles, compliance policies, apps) are applied before the user reaches the desktop.

1. **User desktop:** The user reaches the desktop with a fully configured device.

> [!NOTE]
> Resetting SEA-DEV3 and completing a live Autopilot OOBE takes 20–30 minutes and is beyond the scope of this lab. However, you've completed all the prerequisites (hardware hash registration, profile creation, and assignment) required for Autopilot deployment.

**You now understand the Windows Autopilot deployment workflow.**

---

## Lab Summary

Congratulations! You've completed Lab 01: Foundation — Identity, enrollment, and Autopilot.

In this lab, you accomplished the following:

**Exercise 1: Configure users and groups**
- Reviewed existing Contoso users and verified licensing
- Created two additional test users
- Created an assigned security group for pilot users
- Created dynamic user and device groups for policy targeting

**Exercise 2: Configure administrative delegation**
- Assigned the Intune Administrator role
- Assigned the Cloud Device Administrator role
- Created an administrative unit and scoped administrative access
- Created the `Pharmacy` Intune scope tag and the `Pharmacy Helpdesk` custom Intune role (threaded across Labs 02–06)

**Exercise 3: Configure device registration and settings**
- Configured device join settings in Microsoft Entra ID
- Added additional local administrators for Microsoft Entra joined devices
- Enabled Microsoft Entra LAPS for local administrator password management

**Exercise 4: Configure Windows enrollment policies**
- Verified automatic Intune enrollment for the tenant
- Configured the Default Enrollment Status Page to gate the first-run experience
- Created a stricter, blocking Enrollment Status Page profile for the pilot group
- Reviewed default enrollment restrictions
- Created and assigned a device limit restriction policy
- Blocked personally owned Android enrollment with a custom platform restriction

**Exercise 5: Enroll Windows devices**
- Enrolled SEA-DEV1 (as Megan Bowen) via Microsoft Entra join
- Enrolled SEA-DEV2 (as Joni Sherman) via Microsoft Entra join
- Verified both devices in Intune and dynamic group membership

**Exercise 6: Configure Windows Autopilot**
- Generated the Autopilot hardware hash for SEA-DEV3
- Uploaded the hardware hash to Intune
- Created a Windows Autopilot deployment profile
- Assigned the profile to SEA-DEV3

**Key Takeaways:**
- Microsoft Entra ID is the foundation for modern device management—devices must be joined or registered before enrolling in Intune
- Dynamic groups automate policy targeting based on user or device attributes; compound rules using `-and`/`-or` are the canonical pattern for regulatory or per-region scoping
- Microsoft Entra ID roles + administrative units delegate Entra-level permissions; Intune has a **separate** RBAC system with **custom roles + scope tags** for delegating policy and device administration
- Scope tags created on day one (Pharmacy) thread through every Intune object you create later — apply them at policy creation time to keep the delegated admin model intact
- In modern cloud-only tenants, automatic Intune enrollment is on by default; explicit MDM-scope configuration is primarily a hybrid identity and co-management concern
- The Enrollment Status Page is what shapes the user's first-run experience—use targeted, prioritized profiles to give pilot users a stricter, blocking experience and standard users a faster sign-in
- Device platform restrictions are the safety net against unauthorized platforms or ownership types (e.g., personal Android blocked, corporate Android Enterprise allowed)
- Windows Autopilot streamlines device provisioning by pre-registering devices and applying deployment profiles during OOBE

**Next Steps:**
The devices you enrolled in this lab (SEA-DEV1 and SEA-DEV2) will be used in subsequent labs to deploy configuration profiles, compliance policies, applications, and security baselines. Lab 02 focuses on managing and maintaining these devices using Intune policies.

---

**END OF LAB**
