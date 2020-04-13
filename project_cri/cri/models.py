# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib import admin

class CriProject(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', unique=True, max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CRI_PROJECT'

class CriProjectAdmin(admin.ModelAdmin):
    list_display = ['id' , 'name']



class CriBranch(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    project = models.ForeignKey(CriProject, models.DO_NOTHING, db_column='PROJECT_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CRI_BRANCH'

class CriBranchAdmin(admin.ModelAdmin):
    list_display = ['name','proj']
    def proj(self, obj):
        return  obj.project.name
    proj.short_description = 'Project'
    proj.admin_order_field = 'project__name'


class CriServer(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', unique=True, max_length=100)  # Field name made lowercase.
    path = models.CharField(db_column='PATH', max_length=1000)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CRI_SERVER'
class CriHostAdmin(admin.ModelAdmin):
    list_display = ['name','path']

class CriServerAdmin(admin.ModelAdmin):
    list_display = ['name','path']

class CriRefinementType(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', unique=True, max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CRI_REFINEMENT_TYPE'

class CriRefinementTypeAdmin(admin.ModelAdmin):
    list_display = ['name']


class CriRefinementState(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', unique=True, max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CRI_REFINEMENT_STATE'

class CriRefinementStateAdmin(admin.ModelAdmin):
    list_display = ['name']

class CriProjectConfig(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    project = models.OneToOneField(CriProject, models.DO_NOTHING, db_column='PROJECT_ID')  # Field name made lowercase.
    jenkins_url = models.CharField(db_column='JENKINS_URL', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    jenkins_user = models.CharField(db_column='JENKINS_USER', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    jenkins_apitoken = models.CharField(db_column='JENKINS_APITOKEN', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    jenkins_scheduler = models.CharField(db_column='JENKINS_SCHEDULER', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    jenkins_controller = models.CharField(db_column='JENKINS_CONTROLLER', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    jenkins_credential_id = models.CharField(db_column='JENKINS_CREDENTIAL_ID', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    jenkins_node_label = models.CharField(db_column='JENKINS_NODE_LABEL', max_length=2000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CRI_PROJECT_CONFIG'


class CriProjectConfigAdmin(admin.ModelAdmin):
    #model = CriProjectConfig
    list_display = ['proj','jenkins_url','jenkins_user','jenkins_apitoken','jenkins_scheduler','jenkins_controller','jenkins_credential_id','jenkins_node_label']
    def proj(self, obj):
        return  obj.project.name
    proj.short_description = 'Project'
    proj.admin_order_field = 'project__name'

class CriBranchConfig(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    branch = models.OneToOneField(CriBranch, models.DO_NOTHING, db_column='BRANCH_ID')  # Field name made lowercase.
    auto = models.IntegerField(db_column='AUTO')  # Field name made lowercase.
    s2c = models.IntegerField(db_column='S2C')  # Field name made lowercase.
    manual = models.IntegerField(db_column='MANUAL')  # Field name made lowercase.
    allowed_conflict_count = models.IntegerField(db_column='ALLOWED_CONFLICT_COUNT', blank=True, null=True)  # Field name made lowercase.
    allowed_build_duration = models.IntegerField(db_column='ALLOWED_BUILD_DURATION', blank=True, null=True)  # Field name made lowercase.
    allowed_iterations = models.IntegerField(db_column='ALLOWED_ITERATIONS', blank=True, null=True)  # Field name made lowercase.
    evo_project = models.CharField(db_column='EVO_PROJECT', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    mirror_sites = models.CharField(db_column='MIRROR_SITES', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    publish_root = models.CharField(db_column='PUBLISH_ROOT', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    space_required = models.IntegerField(db_column='SPACE_REQUIRED', blank=True, null=True)  # Field name made lowercase.
    sb_create = models.CharField(db_column='SB_CREATE', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    sb_pre_build = models.CharField(db_column='SB_PRE_BUILD', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    sb_build = models.CharField(db_column='SB_BUILD', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    sb_post_build = models.CharField(db_column='SB_POST_BUILD', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    lastest_refinement_lg = models.CharField(db_column='LASTEST_REFINEMENT_LG', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CRI_BRANCH_CONFIG'


class CriBranchConfigAdmin(admin.ModelAdmin):
    #model = CriProjectConfig
    list_display = ['cr_branch','publish_root','auto','s2c','manual','allowed_conflict_count','allowed_build_duration','evo_project','mirror_sites','space_required','sb_create','sb_build','sb_post_build','lastest_refinement_lg']
    def cr_branch(self, obj):
        return  obj.branch.name
    cr_branch.short_description = 'branch'
    cr_branch.admin_order_field = 'branch__name'


class CriRequest(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    branch = models.ForeignKey(CriBranch, models.DO_NOTHING, db_column='BRANCH_ID')  # Field name made lowercase.
    project = models.ForeignKey(CriProject, models.DO_NOTHING, db_column='PROJECT_ID')  # Field name made lowercase.
    patch = models.CharField(db_column='PATCH', max_length=200, blank=True, null=True)  # Field name made lowercase.
    s2c_id = models.IntegerField(db_column='S2C_ID', blank=True, null=True)  # Field name made lowercase.
    refinement_type = models.ForeignKey(CriRefinementType, models.DO_NOTHING, db_column='REFINEMENT_TYPE_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CRI_REQUEST'

class crirequest(admin.ModelAdmin):
    list_display = ['request_id', 'c_branch','c_project','c_rtype','s2c_id']
    def request_id(self,obj):
        return obj.id
    request_id.short_description = 'request_id'

    def c_branch(self,obj):
        return obj.branch.name
    c_branch.short_description = 'branch'

    def c_project(self,obj):
        return obj.project.name
    c_project.short_description = 'branch'

    def c_rtype(self,obj):
        return obj.refinement_type.name
    c_rtype.short_description = 'refinement_type'

class CriStatus(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    refinement_iteration = models.IntegerField(db_column='REFINEMENT_ITERATION', blank=True, null=True)  # Field name made lowercase.
    request = models.ForeignKey(CriRequest, models.DO_NOTHING, db_column='REQUEST_ID')  # Field name made lowercase.
    jenkins_job_url = models.CharField(db_column='JENKINS_JOB_URL', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    server = models.CharField(db_column='SERVER', max_length=256, blank=True, null=True)  # Field name made lowercase.
    sb_path = models.CharField(db_column='SB_PATH', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    create_duration = models.IntegerField(db_column='CREATE_DURATION', blank=True, null=True)  # Field name made lowercase.
    patch_status = models.ForeignKey(CriRefinementState, models.DO_NOTHING, db_column='PATCH_STATUS', related_name='+' )  # Field name made lowercase.
    patch_duration = models.IntegerField(db_column='PATCH_DURATION')  # Field name made lowercase.
    ea_build_url = models.CharField(db_column='EA_BUILD_URL', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    conflicts = models.IntegerField(db_column='CONFLICTS', blank=True, null=True)  # Field name made lowercase.
    build_duration = models.IntegerField(db_column='BUILD_DURATION', blank=True, null=True)  # Field name made lowercase.
    patch_owner = models.CharField(db_column='PATCH_OWNER', max_length=20, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='NOTES', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    refinement_state = models.ForeignKey(CriRefinementState, models.DO_NOTHING, db_column='REFINEMENT_STATE_ID', related_name='+' )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CRI_STATUS'
