# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools


class Register(models.Model):
    _name = "af_register"
    _description = "Registro de clientes nuevos"
    # _order = "priority desc, id desc"
    # _inherit = ['mail.thread.cc',
    #             'mail.thread.blacklist',
    #             'mail.thread.phone',
    #             'mail.activity.mixin',
    #             'utm.mixin',
    #             'format.address.mixin',
    #             'mail.tracking.duration.mixin',
    #            ]
    # _primary_email = 'email_from'
    # _check_company_auto = True
    # _track_duration_field = 'stage_id'

    # Description
    name = fields.Char(
        'Opportunity'
        # , index='trigram', required=True,
        # compute='_compute_name', readonly=False, store=True
        )
    
    # user_id = fields.Many2one(
    #     'res.users', string='Salesperson', default=lambda self: self.env.user,
    #     domain="[('share', '=', False)]",
    #     check_company=True, index=True, tracking=True)
    # # user_company_ids = fields.Many2many(
    #     'res.company', compute='_compute_user_company_ids',
    #     help='UX: Limit to lead company or all if no company')
    # team_id = fields.Many2one(
    #     'crm.team', string='Sales Team', check_company=True, index=True, tracking=True,
    #     compute='_compute_team_id', ondelete="set null", readonly=False, store=True, precompute=True)
    # lead_properties = fields.Properties(
    #     'Properties', definition='team_id.lead_properties_definition',
    #     copy=True)
    # company_id = fields.Many2one(
    #     'res.company', string='Company', index=True,
    #     compute='_compute_company_id', readonly=False, store=True)
    # referred = fields.Char('Referred By')
    # description = fields.Html('Notes')
    # active = fields.Boolean('Active', default=True, tracking=True)
    # type = fields.Selection([
    #     ('lead', 'Lead'), ('opportunity', 'Opportunity')], required=True, tracking=15, index=True,
    #     default=lambda self: 'lead' if self.env['res.users'].has_group('crm.group_use_lead') else 'opportunity')
    # # Pipeline management
    # priority = fields.Selection(
    #     crm_stage.AVAILABLE_PRIORITIES, string='Priority', index=True,
    #     default=crm_stage.AVAILABLE_PRIORITIES[0][0])
    # stage_id = fields.Many2one(
    #     'crm.stage', string='Stage', index=True, tracking=True,
    #     compute='_compute_stage_id', readonly=False, store=True,
    #     copy=False, group_expand='_read_group_stage_ids', ondelete='restrict',
    #     domain="['|', ('team_id', '=', False), ('team_id', '=', team_id)]")
    # kanban_state = fields.Selection([
    #     ('grey', 'No next activity planned'),
    #     ('red', 'Next activity late'),
    #     ('green', 'Next activity is planned')], string='Kanban State',
    #     compute='_compute_kanban_state')
    # tag_ids = fields.Many2many(
    #     'crm.tag', 'crm_tag_rel', 'lead_id', 'tag_id', string='Tags',
    #     help="Classify and analyze your lead/opportunity categories like: Training, Service")
    # color = fields.Integer('Color Index', default=0)
    # # Revenues
    # expected_revenue = fields.Monetary('Expected Revenue', currency_field='company_currency', tracking=True)
    # prorated_revenue = fields.Monetary('Prorated Revenue', currency_field='company_currency', store=True, compute="_compute_prorated_revenue")
    # recurring_revenue = fields.Monetary('Recurring Revenues', currency_field='company_currency', tracking=True)
    # recurring_plan = fields.Many2one('crm.recurring.plan', string="Recurring Plan")
    # recurring_revenue_monthly = fields.Monetary('Expected MRR', currency_field='company_currency', store=True,
    #                                             compute="_compute_recurring_revenue_monthly")
    # recurring_revenue_monthly_prorated = fields.Monetary('Prorated MRR', currency_field='company_currency', store=True,
    #                                                      compute="_compute_recurring_revenue_monthly_prorated")
    # recurring_revenue_prorated = fields.Monetary('Prorated Recurring Revenues', currency_field='company_currency',
    #                                              compute="_compute_recurring_revenue_prorated", store=True)
    # company_currency = fields.Many2one("res.currency", string='Currency', compute="_compute_company_currency", compute_sudo=True)
    # # Dates
    # date_closed = fields.Datetime('Closed Date', readonly=True, copy=False)
    # date_automation_last = fields.Datetime('Last Action', readonly=True)
    # date_open = fields.Datetime(
    #     'Assignment Date', compute='_compute_date_open', readonly=True, store=True)
    # day_open = fields.Float('Days to Assign', compute='_compute_day_open', store=True)
    # day_close = fields.Float('Days to Close', compute='_compute_day_close', store=True)
    # date_last_stage_update = fields.Datetime(
    #     'Last Stage Update', compute='_compute_date_last_stage_update', index=True, readonly=True, store=True)
    # date_conversion = fields.Datetime('Conversion Date', readonly=True)
    # date_deadline = fields.Date('Expected Closing', help="Estimate of the date on which the opportunity will be won.")
    # # Customer / contact
    # partner_id = fields.Many2one(
    #     'res.partner', string='Customer', check_company=True, index=True, tracking=10,
    #     help="Linked partner (optional). Usually created when converting the lead. You can find a partner by its Name, TIN, Email or Internal Reference.")
    # partner_is_blacklisted = fields.Boolean('Partner is blacklisted', related='partner_id.is_blacklisted', readonly=True)
    # contact_name = fields.Char(
    #     'Contact Name', index='trigram', tracking=30,
    #     compute='_compute_contact_name', readonly=False, store=True)
    # partner_name = fields.Char(
    #     'Company Name', index='trigram', tracking=20,
    #     compute='_compute_partner_name', readonly=False, store=True,
    #     help='The name of the future partner company that will be created while converting the lead into opportunity')
    # function = fields.Char('Job Position', compute='_compute_function', readonly=False, store=True)
    # title = fields.Many2one('res.partner.title', string='Title', compute='_compute_title', readonly=False, store=True)
    # email_from = fields.Char(
    #     'Email', tracking=40, index='trigram',
    #     compute='_compute_email_from', inverse='_inverse_email_from', readonly=False, store=True)
    # email_normalized = fields.Char(index='trigram')  # inherited via mail.thread.blacklist
    # email_domain_criterion = fields.Char(
    #     string='Email Domain Criterion',
    #     compute="_compute_email_domain_criterion",
    #     index='btree_not_null',  # used for exact match, void value do not matter
    #     store=True,
    #     unaccent=False,  # normalized, exact matching
    # )
    # phone = fields.Char(
    #     'Phone', tracking=50,
    #     compute='_compute_phone', inverse='_inverse_phone', readonly=False, store=True)
    # mobile = fields.Char('Mobile', compute='_compute_mobile', readonly=False, store=True)
    # phone_sanitized = fields.Char(index='btree_not_null')  # inherited via mail.thread.phone
    # phone_state = fields.Selection([
    #     ('correct', 'Correct'),
    #     ('incorrect', 'Incorrect')], string='Phone Quality', compute="_compute_phone_state", store=True)
    # email_state = fields.Selection([
    #     ('correct', 'Correct'),
    #     ('incorrect', 'Incorrect')], string='Email Quality', compute="_compute_email_state", store=True)
    # website = fields.Char('Website', help="Website of the contact", compute="_compute_website", readonly=False, store=True)
    # lang_id = fields.Many2one(
    #     'res.lang', string='Language',
    #     compute='_compute_lang_id', readonly=False, store=True)
    # lang_code = fields.Char(related='lang_id.code')
    # lang_active_count = fields.Integer(compute='_compute_lang_active_count')
    # # Address fields
    # street = fields.Char('Street', compute='_compute_partner_address_values', readonly=False, store=True)
    # street2 = fields.Char('Street2', compute='_compute_partner_address_values', readonly=False, store=True)
    # zip = fields.Char('Zip', change_default=True, compute='_compute_partner_address_values', readonly=False, store=True)
    # city = fields.Char('City', compute='_compute_partner_address_values', readonly=False, store=True)
    # state_id = fields.Many2one(
    #     "res.country.state", string='State',
    #     compute='_compute_partner_address_values', readonly=False, store=True,
    #     domain="[('country_id', '=?', country_id)]")
    # country_id = fields.Many2one(
    #     'res.country', string='Country',
    #     compute='_compute_partner_address_values', readonly=False, store=True)
    # # Probability (Opportunity only)
    # probability = fields.Float(
    #     'Probability', group_operator="avg", copy=False,
    #     compute='_compute_probabilities', readonly=False, store=True)
    # automated_probability = fields.Float('Automated Probability', compute='_compute_probabilities', readonly=True, store=True)
    # is_automated_probability = fields.Boolean('Is automated probability?', compute="_compute_is_automated_probability")
    # # Won/Lost
    # lost_reason_id = fields.Many2one(
    #     'crm.lost.reason', string='Lost Reason',
    #     index=True, ondelete='restrict', tracking=True)
    # # Statistics
    # calendar_event_ids = fields.One2many('calendar.event', 'opportunity_id', string='Meetings')
    # duplicate_lead_ids = fields.Many2many("crm.lead", compute="_compute_potential_lead_duplicates", string="Potential Duplicate Lead", context={"active_test": False})
    # duplicate_lead_count = fields.Integer(compute="_compute_potential_lead_duplicates", string="Potential Duplicate Lead Count")
    # meeting_display_date = fields.Date(compute="_compute_meeting_display")
    # meeting_display_label = fields.Char(compute="_compute_meeting_display")
    # # UX
    # partner_email_update = fields.Boolean('Partner Email will Update', compute='_compute_partner_email_update')
    # partner_phone_update = fields.Boolean('Partner Phone will Update', compute='_compute_partner_phone_update')
    # is_partner_visible = fields.Boolean('Is Partner Visible', compute='_compute_is_partner_visible')
    # # UTMs - enforcing the fact that we want to 'set null' when relation is unlinked
    # campaign_id = fields.Many2one(ondelete='set null')
    # medium_id = fields.Many2one(ondelete='set null')
    # source_id = fields.Many2one(ondelete='set null')

    # _sql_constraints = [
    #     ('check_probability', 'check(probability >= 0 and probability <= 100)', 'The probability of closing the deal should be between 0% and 100%!')
    # ]

    