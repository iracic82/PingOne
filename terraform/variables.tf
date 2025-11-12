variable "aws_region" {
  type    = string
  default = "eu-central-1"
}

variable "vpc_cidr" {
  type    = string
  default = "10.100.0.0/16"
}

variable "subnet_a_cidr" {
  type    = string
  default = "10.100.1.0/24"
}

variable "subnet_b_cidr" {
  type    = string
  default = "10.100.2.0/24"
}

variable "windows_admin_password" {
  description = "Password for the Windows Administrator account"
  type        = string
  sensitive   = true
}
variable "aws_ec2_key_pair_name" {
  description = "Name for the EC2 SSH key pair"
  type        = string
  default     = "instruqt-demo-key"
}
# Sandbox/Student ID
  variable "sandbox_id" {
    description = "Instruqt sandbox/participant ID"
    type        = string
    default     = "1"
  }

  # LDAP Configuration
  variable "ldap_base_dn" {
    description = "LDAP base DN"
    type        = string
    default     = "DC=acme,DC=corp"
  }

  variable "ldap_server" {
    description = "LDAP server URL"
    type        = string
    default     = "ldaps://ad.highvelocitynetworking.com:636"
  }

  variable "ldap_user_search_base" {
    description = "LDAP user search base"
    type        = string
    default     = "OU=CorpA,DC=acme,DC=corp"
  }

  variable "ldap_bind_dn" {
    description = "LDAP bind DN for service account"
    type        = string
    default     = "CN=PingOne Service,CN=Users,DC=acme,DC=corp"
    sensitive   = true
  }

  variable "ldap_bind_password" {
    description = "LDAP bind password"
    type        = string
    default     = "Test123!"
    sensitive   = true
  }

  # PingOne Configuration
  variable "pingone_admin_env_id" {
    description = "PingOne admin environment ID"
    type        = string
    default     = "3ac89109-409f-4ba8-8299-e7789157b283"
  }

  variable "pingone_application_id" {
    description = "PingOne application ID"
    type        = string
    default     = "6a92b141-0192-4247-9663-a40792bbc0ac"
  }

  variable "pingone_client_id" {
    description = "PingOne worker app client ID"
    type        = string
    default     = "2a083469-ee26-46b0-91c8-4ed8bab49432"
  }

  variable "pingone_client_secret" {
    description = "PingOne worker app client secret"
    type        = string
    default     = "ydiTaDE00egkyM6JCQN_MMXl8qN4dPHoqDFNcHMXpPHejrWCu.siz~odx52OMTBX"
    sensitive   = true
  }

  variable "pingone_client_secret_app" {
    description = "PingOne application client secret"
    type        = string
    default     = "fSn_06zh.-063HO.llPgIBlL.PFo7VLEDBKzachC~YK9dg9sI_ELL_zUY8F-WweM"
    sensitive   = true
  }

  variable "pingone_issuer" {
    description = "PingOne issuer URL"
    type        = string
    default     = "https://auth.pingone.com/76c431af-e4c2-40e9-8198-0b373f232253/as"
  }

  variable "pingone_target_env_id" {
    description = "PingOne target environment ID"
    type        = string
    default     = "76c431af-e4c2-40e9-8198-0b373f232253"
  }

  # AWS Configuration
  variable "ad_security_group_id" {
    description = "AD server security group ID"
    type        = string
    default     = "sg-09829deacde96c801"
  }

  variable "aws_region_target" {
    description = "AWS region for portal resources"
    type        = string
    default     = "eu-central-1"
  }

 
