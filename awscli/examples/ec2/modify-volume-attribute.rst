**To modify a volume attribute**

This example sets the ``autoEnableIo`` attribute of the volume with the ID ``vol-1a2b3c4d`` to ``true``.

Command::

  aws ec2 modify-volume-attribute --volume-id vol-1a2b3c4d --auto-enable-io

Output::

   {
       "return": "true"
   }