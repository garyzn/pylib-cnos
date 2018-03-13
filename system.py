from connect import *
import json

class System(object):
    """
        Provides a class implementation and methods for managing and setting up
        images and config files on the node. This class presents an abstraction.
    """
    def __init__(self):
        self.cfg = '/nos/api'

    def download_boot_img(self, conn, params):
        '''
            This API downloads a boot image to the switch

            parameters:
            conn - connection object to the node
            params - dictionary that requires the following format of key-value pairs
                    {
                     "protocol":"<protocol>",
                     "serverip":"<serverip>",
                     "srcfile":"<srcfile>",
                     "imgtype":"<imgtype>",
                     "username":"<username>",
                     "passwd":"<passwd>",
                     "vrf_name":"<vrf_name>"
                    } 
            
            description -
            protocol :Protocol name; one of "tftp", "sftp".
            serverip :Server IP address.
            srcfile  :Source file; up to 256 characters long.
            imgtype  :System image type; one of "all", "boot", "onie", "os".
            username :Username for the server. Not required for TFTP.
            passwd   :Password for the server username. Not required for TFTP.
            vrf_name :(Optional) VRF name; an alphabetic string up to 64 characters long

            return : TODO
 
        '''
        restapi = self.cfg + '/download/image'
#url = form_url(conn, restapi)
#hdr = form_hdr(conn)
        return conn.put(restapi, params)

    def put_startup_sw(self, conn, params):
        '''
            This API updates the system startup image
            
            
            parameters:
            conn - connection object to the node
            params - dictionary that requires the following format of key-value pairs
                 {
                     "boot software" : "<setting>"
                 }
            description -
            setting :Next startup image setting; one of "active" or "standby"
            
            return: JSON response    
        '''
        restapi = self.cfg + '/startup/software'
        return conn.put(restapi, params)

    def get_startup_sw(self, conn):
        '''
            This API gets the system startup image.
            
            
            parameters:
            conn - connection object to the node
            
            return: JSON response    
        '''
        restapi = self.cfg + '/startup/software'
        return conn.get(restapi)

    def reset_switch(self, conn):
        '''
            This API resets the switch
            
            
             parameters:
             conn - connection object to the node
            
             return: JSON response
        '''
        restapi = self.cfg + '/reset'
        return conn.get(restapi)

    def download_sw_config(self, params):
        '''
            This API downloads a configuration to the switch
            
            
             parameters:
             conn - connection object to the node
             params - dictionary that requires the following format of key-value pairs
                  {
                    "protocol":"<protocol>",
                    "serverip":"<serverip>",
                    "srcfile":"<srcfile>",
                    "dstfile":"<dstfile>",
                    "username":"<username>",
                    "passwd":"<passwd>",
                    "vrf_name":"<vrf_name>"
                  }
             description -
             protocol :Protocol name; one of "tftp", "sftp".
             serverip :Server IP address.
             srcfile  :Source file; up to 256 characters long.
             dstfile  :Destination file; one of 'running_config', 'startup_config'.
             username :(Optional) Username for the server.
             passwd   :(Optional) Password for the server username.
             vrf_name :(Optional) VRF name; an alphabetic string up to 64 characters long
            
             return: JSON response
        '''
        restapi = self.cfg + '/download/config'
        return conn.post(restapi, params)

    def save_config(self, conn):
        '''
             This API saves the running configuration to the flash memory
             
             
              parameters:
              conn - connection object to the node
             
              return: JSON response
        '''
        restapi = self.cfg + '/save/config'
        return conn.get(restapi)

    def upload_sw_config(self, conn, params):
        '''
           This API uploads a configuration file from the switch to the server
           
           
            parameters:
            conn - connection object to the node
            params - dictionary that requires the following format of key-value pairs
                 {
                   "protocol":"<protocol>",
                   "serverip":"<serverip>",
                   "srcfile":"<srcfile>",
                   "dstfile":"<dstfile>",
                   "username":"<username>",
                   "passwd":"<passwd>",
                   "vrf_name":"<vrf_name>"
                 }
            description -
            protocol :Protocol name; one of "tftp", "sftp".
            serverip :Server IP address.
            srcfile  :Source file; up to 256 characters long.
            dstfile  :Destination file; one of 'running_config', 'startup_config'.
            username :(Optional) Username for the server.
            passwd   :(Optional) Password for the server username.
            vrf_name :(Optional) VRF name; an alphabetic string up to 64 characters long
           
            return: JSON response    
        '''
        restapi = self.cfg + '/upload/config'
        return conn.post(restapi, params)

    def upload_tech_support(self, conn, params):
        '''
           This API uploads technical support information from the switch to the server
           
           
            parameters:
            conn - connection object to the node
            params - dictionary that requires the following format of key-value pairs
                 {
                   "protocol":"<protocol>",
                   "serverip":"<serverip>",
                   "dstfile":"<dstfile>",
                   "username":"<username>",
                   "passwd":"<passwd>",
                   "vrf_name":"<vrf_name>"
                 }
            description -
            protocol :Protocol name; one of "tftp", "sftp".
            serverip :Server IP address.
            dstfile  :Destination file; one of 'running_config', 'startup_config'.
            username :(Optional) Username for the server.
            passwd   :(Optional) Password for the server username.
            vrf_name :(Optional) VRF name; an alphabetic string up to 64 characters long
           
            return: JSON response    
        '''
        restapi = '/upload/tech_support'
        return conn.post(restapi, params)

    def get_transfer_status(self, conn, action, content):
        '''
           This API gets the status of a downloading transfer.
           
           
            parameters:
            conn - connection object to the node
            content - One of 'image', 'running_config', 'startup_config'
            action - 'upload' or 'download'
           
            return: JSON response    
        '''
        restapi = self.cfg + '/' + action + '/status/' + content
        return conn.get(restapi)

    def get_hostname(self, conn):
        '''
           This API gets the hostname of the system
           
           
            parameters:
            conn - connection object to the node
           
            return: JSON response 
        '''
        restapi = self.cfg + '/cfg/hostname'
        return conn.get(restapi)

    def set_hostname(self, params):
        '''
           This API sets the system boot image.
           
           
            parameters:
            conn - connection object to the node
            params - dictionary that requires the following format of key-value pairs
                            {
                                "hostname":"<hostname>"
                            }
            description - 
            hostname :The hostname of the system; a string from 1-64 characters long                    
           
            return: JSON response    
        '''
        restapi = self.cfg + '/cfg/hostname'
        return conn.put(conn, params)

    def get_clock(self, conn):
        '''
            This API gets the date of the system
            
            
             parameters:
             conn - connection object to the node
            
             return: JSON response
        '''
        restapi = self.cfg + '/cfg/clock'
        return conn.get(conn)

    def set_clock(self, conn):
        '''
            This API sets the system date.
            
            
             parameters:
             conn - connection object to the node
             params - dictionary that requires the following format of key-value pairs
                             {
                      #                       "time": "<HH:MM:SS>" ,
                      #                       "day": <day>,
                      #                       "month": <month> ,
                      #                       "year": <year>
                      #                  }
             description - 
             time  :System time in the format "HH:MM:SS".
             day   :The day of the month; an integer from 1-31.
             month :The month; one of the following case-insensitive strings:
              January
              February
              March
              April
              May
              June
              July
              August
              September
              October
              November
              December
             year  :The year; an integer from 2000-2030.
            
              return: JSON response    
        '''
        restapi = self.cfg + '/cfg/clock'
        return conn.put(restapi, params)

    def set_clock_format(self, conn, params):
        '''
             This API sets the clock format to 12 hour or 24 hour format.
             
             
              parameters:
              conn - connection object to the node
              params - dictionary that requires the following format of key-value pairs
               {
                    "format": <format>
               }
              description - 
              format :System clock format; one of:
                       12 (12 hour format)
                       24 (24 hour format)
             
              return: JSON response     
        '''
        restapi = self.cfg + '/cfg/clock/format/'
        return conn.put(restapi, params)

    def set_clock_protocol(self, conn, params):
        '''

             This API sets the protocol to either manual or Network Time Protocol.
             
             
              parameters:
              conn - connection object to the node
              params - dictionary that requires the following format of key-value pairs
                              {
                                "protocol": "<protocol>"
                              }
             description -
             protocol :System clock protocol; one of:
                       none - the clock is manually configured
                       ntp - the clock is configured through NTP
                   Default value: "ntp"
             
             return: JSON response
        '''
        restapi = self.cfg + '/cfg/clock/protocol/'
        return conn.put(restapi, params)

    def set_clock_timezone(self, conn, params):
        '''
             This API sets the clock time zone for the switch
             
             
              parameters:
              conn - connection object to the node
              params - dictionary that requires the following format of key-value pairs
                              {
                                ""timezone": "<timezone>",
                                 "offsethour": "<offsethour>",
                                 "offsetmin": "<lag_mode>",
                              }
             description -
             timezone   :One to five letter string denoting the local system time zone.
             offsethour :Hours offset from UTC; an integer from -23 through 23.
             offsetmin  :Minutes offset from UTC; an integer from 0-59. 
             
             return: JSON response
        '''
        restapi = self.cfg + '/cfg/clock/timezone/'
        return conn.put(restapi, params)

    def get_device_contact(self, conn):
        '''
             This API gets the device contact.
             
             
              parameters:
              conn - connection object to the node
             
              return: JSON response
        '''
        restapi = self.cfg + '/cfg/contact'
        return conn.get(conn)

    def get_device_descr(self, conn):
        '''
            This API gets the device descr.
            
            
             parameters:
             conn - connection object to the node
            
             return: JSON response

        '''
        restapi = self.cfg + '/cfg/descr'
        return conn.get(conn)

    def set_device_descr(self, conn, params):
        '''
           This API updates the device description.
           
           
            parameters:
            conn - connection object to the node
            params - dictionary that requires the following format of key-value pairs
            {
                "descr": <descr>
            }
            description - 
            descr   :Device description; a string up to 256 characters long.
           
            return: JSON response
        '''
        restapi = self.cfg + '/cfg/descr'
        return conn.put(conn, params)

    def set_clock_summertime(self, conn, params):
        '''
           This API set the transition to and from a summer time zone adjustment.
           
           
            parameters:
            conn - connection object to the node
            params - dictionary that requires the following format of key-value pairs
                            {
                               "timezone": <time_zone>,
                               "startweek": <start_week>,
                               "startweekday": <start_weekday>,
                               "startmonth": <start_month>,
                               "starttime" :  "<HH:MM>",
                               "endweek"   : <end_week>,
                               "endweekday": <end_weekday>,
                               "endmonth"  : <end_month>,
                               "endtime"   :  "<HH:MM>",
                               "offsetmin" : <minutes>
                            }
            description -
            timezone     :Local time zone of the system; a three to five character
                  string such as "PST", "MST", "CST", or "EST".
            startweek    :Week number in the month in which to start Daylight
                  Saving time; an integer from 1-5 (first week=1, last
                  week=5).
            startweekday :Weekday on which to start DST; one of the following
                  case-insensitive strings:
                      monday - sunday
            startmonth   :Month to start DST; one of the following
                      case-insensitive strings:
                      january - december
            starttime    :Time to start DST; a string in the format "HH:MM".
                      endweek Week number in which to end DST; an integer from
                          1-5 (first week=1, last week=5).
            endweekday   :Weekday on which to end DST; one of the following
                          case-insensitive strings:
                      monday - sunday
            endmonth     :Month in which DST ends; one of the following
                      case-insensitive strings:
                      january - december
            endtime      :Time to end DST; a string in the format "HH:MM"
            offsetmin    :Offset to add, in minutes; an integer from 1-1440.
           
            return: JSON response
        '''
        restapi = self.cfg + '/cfg/clock/summertime'
        return conn.put(conn, params)
