from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from crispy_forms.bootstrap import FormActions

class ContactForm( forms.Form ):
 def __init__( self, *args, **kwargs ):
  super( ContactForm, self ).__init__( *args, **kwargs )
  self.helper = FormHelper( )
  self.helper.form_method = 'post'
  self.helper.add_input( Submit( 'submit', 'Submit', css_class = 'btn-primary' ) )

 name = forms.CharField( max_length = 100, label = '', placeholder='ame' )
 email = forms.EmailField( max_length = 100, label = '', placeholder='Nam' )
 message = forms.CharField( widget = forms.Textarea, label = '', placeholder='Nae' )

 # layout = Layout(
 #  Field( 'name', placeholder = 'Name' ),
 #  Field( 'email', placeholder = 'Email' ),
 #  Field( 'message', placeholder = 'Message' ),
 # )
