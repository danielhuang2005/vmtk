#!/usr/bin/env python

## Program:   VMTK
## Module:    $RCSfile: vmtksurfmesh.py,v $
## Language:  Python
## Date:      $Date: 2005/09/14 09:49:59 $
## Version:   $Revision: 1.6 $

##   Copyright (c) Luca Antiga, David Steinman. All rights reserved.
##   See LICENCE file for details.

##      This software is distributed WITHOUT ANY WARRANTY; without even 
##      the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR 
##      PURPOSE.  See the above copyright notices for more information.


import vtk
import vtkvmtk
import sys

import pypes

vmtksurfmesh = 'vmtkSurfMesh'

class vmtkSurfMesh(pypes.pypeScript):

    def __init__(self):

        pypes.pypeScript.__init__(self)
        
        self.Surface = None
        self.NodeSpacing = 1.0

        self.SetScriptName('vmtksurfmesh')
        self.SetScriptDoc('wrapper around surfmesh surface mesh generator by Gordan Stuhne')
        self.SetInputMembers([
            ['Surface','i','vtkPolyData',1,'','the input surface','vmtksurfacereader'],
            ['NodeSpacing','nodespacing','float',1,'(0.0,)','desired node spacing']
            ])
        self.SetOutputMembers([
            ['Surface','o','vtkPolyData',1,'','the output surface','vmtksurfacewriter']
            ])

    def Execute(self):

        if self.Surface == None:
            self.PrintError('Error: No Surface.')

        surfmesh = vtkvmtk.vtkvmtkSurfMeshWrapper()
        surfmesh.SetInput(self.Surface)
        surfmesh.SetNodeSpacing(self.NodeSpacing)
        surfmesh.Update()

        self.Surface = surfmesh.GetOutput()

        if self.Surface.GetSource():
            self.Surface.GetSource().UnRegisterAllOutputs()

if __name__=='__main__':
    main = pypes.pypeMain()
    main.Arguments = sys.argv
    main.Execute()
