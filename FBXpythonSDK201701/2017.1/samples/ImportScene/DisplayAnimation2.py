
from fbx import *
#from samples.ImportScene.DisplayCommon import *
def DisplayString(pHeader, pValue="" , pSuffix=""):
	lString = pHeader
	lString += str(pValue)
	lString += pSuffix
	print(lString)

def DisplayBool(pHeader, pValue, pSuffix=""):
	lString = pHeader
	if pValue:
		lString += "true"
	else:
		lString += "false"
	lString += pSuffix
	print(lString)

def DisplayInt(pHeader, pValue, pSuffix=""):
	lString = pHeader
	lString += str(pValue)
	lString += pSuffix
	print(lString)

def DisplayDouble(pHeader, pValue, pSuffix=""):
	print("%s%f%s" % (pHeader, pValue, pSuffix))

def Display2DVector(pHeader, pValue, pSuffix=""):
	print("%s%f, %f%s" % (pHeader, pValue[0], pValue[1], pSuffix))

def Display3DVector(pHeader, pValue, pSuffix=""):
	print("%s%f, %f, %f%s" % (pHeader, pValue[0], pValue[1], pValue[2], pSuffix))

def Display4DVector(pHeader, pValue, pSuffix=""):
	print("%s%f, %f, %f, %f%s" % (pHeader, pValue[0], pValue[1], pValue[2], pValue[3], pSuffix))

def DisplayColor(pHeader, pValue, pSuffix=""):
	print("%s%f (red), %f (green), %f (blue)%s" % (pHeader, pValue.mRed, pValue.mGreen, pValue.mBlue, pSuffix))


#from fbx import *

#FBX_FILE_PATH_AND_NAME_AND_EXT="D:/work/FBXSDK/fbxsdk00100/Solder_Model_FBX_ASCII_2016_2017_settings_.fbx"
FBX_FILE_PATH_AND_NAME_AND_EXT="D:/work/FBXSDK/for_yamakawa/SoldierProject/scenes/FBX/Solder_Model_ASCII_2016_2017_motion00200.fbx"
print(u"00100. fbx_manager=========================================================== ")
"""
fbx_manager = FbxManager.Create()
print(u"00200. fbx_scene")

fbx_scene = FbxScene.Create(fbx_manager, "MyScene")

print(u"00300. fbx_importer")
fbx_importer = FbxImporter.Create(fbx_manager, "")
fbx_importer.Initialize(FBX_FILE_PATH_AND_NAME_AND_EXT)

fbx_importer.Destroy()
print(u"end00200. fbx_scene")
fbx_scene.Destroy()
print(u"end 00100. fbx_manager")
fbx_manager.Destroy()

"""



# -*- coding: utf-8 -*-
from maya import cmds 
import maya as maya
import pymel.core as pm
#import Debug
#Debug=Debug.Debug
def DebugLog(strData):
	mystr=strData
	print(mystr)

#===================class Node=========================
class Node() :
	def __init__(self, name, parent) :
		self.name = name
		self.parent = parent
		self.children = None
		self.type = None
	def addChild(self, child) :
		if not self.children : self.children = list()
		self.children.append(child)

def getTypeName(fbxNode) :
	nodeAttr = fbxNode.GetNodeAttribute()
	e = nodeAttr.GetAttributeType()
	sType = "Unknown"
	if FbxNodeAttribute.eNull == e : sType = "Null"
	elif FbxNodeAttribute.eMarker == e : sType = "Marker"
	elif FbxNodeAttribute.eSkeleton == e : sType = "Skeleton"
	elif FbxNodeAttribute.eMesh == e : sType = "Mesh"
	elif FbxNodeAttribute.eNurbs == e : sType = "Nurbs"
	elif FbxNodeAttribute.ePatch == e : sType = "Patch"
	elif FbxNodeAttribute.eCamera == e : sType = "Camera"
	elif FbxNodeAttribute.eLight == e : sType = "Light"
	return sType

def getHierarchy(fbxNode, node) :
	num = fbxNode.GetChildCount()
	print("getHierarchy(fbxNode= "+str(fbxNode)+", node.name= "+str(node.name)+")")
	if 0 == num : return
	for i in range(num) :
		fbxChild = fbxNode.GetChild(i)
		nodeChild = Node(fbxChild.GetName(), node)
		nodeChild.type = getTypeName(fbxChild)
		node.addChild(nodeChild)
		getHierarchy(fbxChild, nodeChild)

def printHierarchy(node, padding) :
	print padding + node.name
	if not node.children : return
	for child in node.children : printHierarchy(child, padding+"  ")

def addTreeItem(item, node) :
	if not node.children : return
	for child in node.children :
		i = QTreeWidgetItem()
		i.setText(0, "%s (%s)"%(child.name, child.type))
		item.addChild(i)
		addTreeItem(i, child)
#===================class Node=========================	
#===================GetMesh =========================	
def GetMesh(node):
	mesh=node.GetMesh();
	print("mesh== "+str(mesh))
	if mesh ==None:
		print("mesh==None")
		
	
#===================GetMesh =========================	
#===================GetKeyCurve=========================	
def GetKeyCurve(fbxImporter,pScene):
	print ("===========GetKeyCurve(pScene= "+str(fbxImporter)+"  pScene="+str(pScene)+" )===========")
	print ("GetKeyCurve(pScene= "+str(fbxImporter)+"  pScene="+str(pScene)+" )")
	#==SDKの1シーンであるFbxScene sceneをルートとして次のようにします：
	#==① アニメーションスタック数取得
	#int nbAnimStacks = pScene->GetSrcObjectCount<FbxAnimStack>()

	print ("----GetKeyCurve( fbxImporter.GetAnimStackCount()= "+str(fbxImporter.GetAnimStackCount())+" -------------------")
	intAnimStacks=0
	intAnimStacks=fbxImporter.GetAnimStackCount()
	print ("----GetKeyCurve------ intAnimStacks= "+str(intAnimStacks)+" -------------------")
	print ("----GetKeyCurve( fbxImporter.GetActiveAnimStackName()= "+str(fbxImporter.GetActiveAnimStackName())+" -------------------")
	#int intAnimStacks = fbxImporter.GetAnimStackCount()
	#print ("nbAnimStacks= "+str(nbAnimStacks))
	#==② アニメーションスタック取得
	#for ( int i = 0; i < nbAnimStacks; i++ )
	#FbxAnimStack* lAnimStack = pScene->GetSrcObject<FbxAnimStack>(i);
	TakeInfoList= [0 for i in range(1)]
	del TakeInfoList[0]
	for i in range(0, intAnimStacks):
		print("for  i="+str(i))
		pTakeInfo=fbxImporter.GetTakeInfo(i);
		print("for  pTakeInfo="+str(pTakeInfo))
		pTakeName = pTakeInfo.mName;
		print("for  pTakeName="+str(pTakeName))
		mImportName = pTakeInfo.mImportName;
		print("for  mImportName="+str(mImportName))
		
		#fbxAnimStack = fbxImporter.GetAnimStackCount(i)
		#print("for  fbxAnimStack="+str(fbxAnimStack));
		TakeInfoList.append(pTakeInfo);
		
	TakeInfoListLen=len(TakeInfoList)
	i=0
	print("TakeInfoListLen= "+str(TakeInfoListLen))
	for i in range(0, TakeInfoListLen):
		print("TakeInfoList[ "+str(i) +"].mName= "+TakeInfoList[i].mName);
		TakeInfo=TakeInfoList[i]
		print ("===========GetAnimationLayer ===========")
	
		#==③ アニメーションレイヤー数を取得
		#int nbAnimLayers = pAnimStack->GetMemberCount<FbxAnimLayer>();
		print("TakeInfo="+str(TakeInfo))
		print("TakeInfo.mName="+str(TakeInfo.mName))
		print("TakeInfo.mCurrentLayer="+str(TakeInfo.mCurrentLayer))
		if(TakeInfo.mCurrentLayer==-1):
			print("TakeInfo.mLayerInfoList=	   AnimLayer	is  None	is  This FBX is None Animation File  !!!!!!!")
		else:
			print("TakeInfo.mLayerInfoList="+str(TakeInfo.mLayerInfoList))
		
	#print("lAnimStack="+str(lAnimStack.))
		#AnimLayers=
	DisplayAnimation(pScene)
"""
	#==④ アニメーションレイヤーを取得
	for ( int i = 0; i < nbAnimLayers; i++ )
　　FbxAnimLayer* pAnimLayer = pAnimStack->GetMember<FbxAnimLayer>(l);
	
	#==⑤ ノードが持っているアニメーションカーブをアニメーションレイヤーから取得
	FbxAnimCurve* pAnimCurve = pNode->LclTranslation.GetCurve(pAnimLayer, FBXSDK_CURVENODE_COMPONENT_X);

	⑥ カーブ内のキータイムを取得
	int nbKeyCount = pAnimCurve->KeyGetCount();
	for ( int i = 0; i < nbAnimLayers; i++ )
	FbxTime keyTime = pAnimCurve->KeyGetTime( nbKeyCount )
"""

#===========================引用　D:\work\FBXSDK\FBX\FBX Python SDK\2016.1.1\samples\ImportScene\DisplayAnimation.py


from fbx import FbxAnimStack

#from fbx import FbxAnimLayer
#from fbx import FbxProperty
#from fbx import FbxNodeAttribute

def DisplayAnimation(pScene):
	print("=============================DisplayAnimation.py===DisplayAnimation(pScene = "+ str(pScene)+")==================================")
	print("FbxAnimStack.ClassId="+str(FbxAnimStack.ClassId))
	pFbxAnimStackClassID=FbxAnimStack.ClassId
	
	print("pFbxAnimStackClassID="+str(pFbxAnimStackClassID))
	
	pFbxCriteriaFbxAnimStackClassID=FbxCriteria.ObjectType(FbxAnimStack.ClassId)
	print("pFbxCriteriaFbxAnimStackClassID="+str(pFbxCriteriaFbxAnimStackClassID))
	#pFbxCriteriaFbxAnimStackClassID=
	#loopCount=pScene.GetSrcObjectCount(pFbxAnimStackClassID)
	intSceneAllObjCount=pScene.GetSrcObjectCount(pFbxCriteriaFbxAnimStackClassID)
	print("intSceneAllObjCount="+str(intSceneAllObjCount))
	#for i in range(pScene.GetSrcObjectCount(FbxAnimStack.ClassId)):
	for i in range(intSceneAllObjCount):
		print("DisplayAnimation  i="+str(i))
		lAnimStack = pScene.GetSrcObject(pFbxCriteriaFbxAnimStackClassID, i)
		print("lAnimStack  ="+str(lAnimStack))
		
		lOutputString = "Animation Stack Name: "
		lOutputString += lAnimStack.GetName()
		lOutputString += "\n"
		print(lOutputString)
		DisplayAnimationStack(lAnimStack, pScene.GetRootNode(), True)
		
		
	"""
	for i in range(pScene.GetSrcObjectCount(FbxAnimStack.ClassId)):
		lAnimStack = pScene.GetSrcObject(FbxAnimStack.ClassId, i)

		lOutputString = "Animation Stack Name: "
		lOutputString += lAnimStack.GetName()
		lOutputString += "\n"
		print(lOutputString)

		DisplayAnimationStack(lAnimStack, pScene.GetRootNode(), False)
	"""
def DisplayAnimationStack(pAnimStack, pNode, isSwitcher):
	print("============DisplayAnimationStack======================")
	pFbxCriteria_FbxAnimLayer=FbxCriteria.ObjectType(FbxAnimLayer.ClassId)
	print("pFbxCriteria_FbxAnimLayer="+str(pFbxCriteria_FbxAnimLayer))
	nbAnimLayers = pAnimStack.GetSrcObjectCount(pFbxCriteria_FbxAnimLayer)

	lOutputString = "Animation stack contains "
	lOutputString += str(nbAnimLayers)
	lOutputString += " Animation Layer(s)"
	print(lOutputString)

	for l in range(nbAnimLayers):
		
		lAnimLayer = pAnimStack.GetSrcObject(pFbxCriteria_FbxAnimLayer, l)

		lOutputString = "AnimLayer "
		lOutputString += str(l)
		print(lOutputString)

		DisplayAnimationLayer(lAnimLayer, pNode, isSwitcher)

def DisplayAnimationLayer(pAnimLayer, pNode, isSwitcher=False):
	lOutputString = "	 Node Name: "
	lOutputString += pNode.GetName()
	lOutputString += "\n"
	print(lOutputString)

	DisplayChannels(pNode, pAnimLayer, DisplayCurveKeys, DisplayListCurveKeys, isSwitcher)
	print

	for lModelCount in range(pNode.GetChildCount()):
		print("lModelCount  loop= "+str(lModelCount))
		
		DisplayAnimationLayer(pAnimLayer, pNode.GetChild(lModelCount), isSwitcher)


def DisplayChannels(pNode, pAnimLayer, DisplayCurve, DisplayListCurve, isSwitcher):
	print("DisplayChannels(pNode ="+str(pNode)+", pAnimLayer="+str(pAnimLayer)+", DisplayCurve="+str(DisplayCurve)+", DisplayListCurve="+str(DisplayListCurve)+", isSwitcher="+str(isSwitcher)+")")
	lAnimCurve = None

	KFCURVENODE_T_X = "X"
	KFCURVENODE_T_Y = "Y"
	KFCURVENODE_T_Z = "Z"

	KFCURVENODE_R_X = "X"
	KFCURVENODE_R_Y = "Y"
	KFCURVENODE_R_Z = "Z"
	KFCURVENODE_R_W = "W"

	KFCURVENODE_S_X = "X"
	KFCURVENODE_S_Y = "Y"
	KFCURVENODE_S_Z = "Z"
	
	# Display general curves.
	if not isSwitcher:
		lAnimCurve = pNode.LclTranslation.GetCurve(pAnimLayer, KFCURVENODE_T_X)
		if lAnimCurve:
			print("		TX")
			DisplayCurve(lAnimCurve)
		lAnimCurve = pNode.LclTranslation.GetCurve(pAnimLayer, KFCURVENODE_T_Y)
		if lAnimCurve:
			print("		TY")
			DisplayCurve(lAnimCurve)
		lAnimCurve = pNode.LclTranslation.GetCurve(pAnimLayer, KFCURVENODE_T_Z)
		if lAnimCurve:
			print("		TZ")
			DisplayCurve(lAnimCurve)

		lAnimCurve = pNode.LclRotation.GetCurve(pAnimLayer, KFCURVENODE_R_X)
		if lAnimCurve:
			print("		RX")
			DisplayCurve(lAnimCurve)
		lAnimCurve = pNode.LclRotation.GetCurve(pAnimLayer, KFCURVENODE_R_Y)
		if lAnimCurve:
			print("		RY")
			DisplayCurve(lAnimCurve)
		lAnimCurve = pNode.LclRotation.GetCurve(pAnimLayer, KFCURVENODE_R_Z)
		if lAnimCurve:
			print("		RZ")
			DisplayCurve(lAnimCurve)

		lAnimCurve = pNode.LclScaling.GetCurve(pAnimLayer, KFCURVENODE_S_X)
		if lAnimCurve:
			print("		SX")
			DisplayCurve(lAnimCurve)
		lAnimCurve = pNode.LclScaling.GetCurve(pAnimLayer, KFCURVENODE_S_Y)
		if lAnimCurve:
			print("		SY")
			DisplayCurve(lAnimCurve)
		lAnimCurve = pNode.LclScaling.GetCurve(pAnimLayer, KFCURVENODE_S_Z)
		if lAnimCurve:
			print("		SZ")
			DisplayCurve(lAnimCurve)
	
	# Display curves specific to a light or marker.
	lNodeAttribute = pNode.GetNodeAttribute()

	KFCURVENODE_COLOR_RED = "X"
	KFCURVENODE_COLOR_GREEN = "Y"
	KFCURVENODE_COLOR_BLUE = "Z"
	
	if lNodeAttribute:
		lAnimCurve = lNodeAttribute.Color.GetCurve(pAnimLayer, KFCURVENODE_COLOR_RED)
		if lAnimCurve:
			print("		Red")
			DisplayCurve(lAnimCurve)
		lAnimCurve = lNodeAttribute.Color.GetCurve(pAnimLayer, KFCURVENODE_COLOR_GREEN)
		if lAnimCurve:
			print("		Green")
			DisplayCurve(lAnimCurve)
		lAnimCurve = lNodeAttribute.Color.GetCurve(pAnimLayer, KFCURVENODE_COLOR_BLUE)
		if lAnimCurve:
			print("		Blue")
			DisplayCurve(lAnimCurve)

		# Display curves specific to a light.
		light = pNode.GetLight()
		if light:
			lAnimCurve = light.Intensity.GetCurve(pAnimLayer)
			if lAnimCurve:
				print("		Intensity")
				DisplayCurve(lAnimCurve)

			lAnimCurve = light.OuterAngle.GetCurve(pAnimLayer)
			if lAnimCurve:
				print("		Cone Angle")
				DisplayCurve(lAnimCurve)

			lAnimCurve = light.Fog.GetCurve(pAnimLayer)
			if lAnimCurve:
				print("		Fog")
				DisplayCurve(lAnimCurve)

		# Display curves specific to a camera.
		camera = pNode.GetCamera()
		if camera:
			lAnimCurve = camera.FieldOfView.GetCurve(pAnimLayer)
			if lAnimCurve:
				print("		Field of View")
				DisplayCurve(lAnimCurve)

			lAnimCurve = camera.FieldOfViewX.GetCurve(pAnimLayer)
			if lAnimCurve:
				print("		Field of View X")
				DisplayCurve(lAnimCurve)

			lAnimCurve = camera.FieldOfViewY.GetCurve(pAnimLayer)
			if lAnimCurve:
				print("		Field of View Y")
				DisplayCurve(lAnimCurve)

			lAnimCurve = camera.OpticalCenterX.GetCurve(pAnimLayer)
			if lAnimCurve:
				print("		Optical Center X")
				DisplayCurve(lAnimCurve)

			lAnimCurve = camera.OpticalCenterY.GetCurve(pAnimLayer)
			if lAnimCurve:
				print("		Optical Center Y")
				DisplayCurve(lAnimCurve)

			lAnimCurve = camera.Roll.GetCurve(pAnimLayer)
			if lAnimCurve:
				print("		Roll")
				DisplayCurve(lAnimCurve)

		# Display curves specific to a geometry.
		if lNodeAttribute.GetAttributeType() == FbxNodeAttribute.eMesh or \
			lNodeAttribute.GetAttributeType() == FbxNodeAttribute.eNurbs or \
			lNodeAttribute.GetAttributeType() == FbxNodeAttribute.ePatch:
			lGeometry = lNodeAttribute

			lBlendShapeDeformerCount = lGeometry.GetDeformerCount(FbxDeformer.eBlendShape)
			for lBlendShapeIndex in range(lBlendShapeDeformerCount):
				lBlendShape = lGeometry.GetDeformer(lBlendShapeIndex, FbxDeformer.eBlendShape)
				lBlendShapeChannelCount = lBlendShape.GetBlendShapeChannelCount()
				for lChannelIndex in range(lBlendShapeChannelCount):
					lChannel = lBlendShape.GetBlendShapeChannel(lChannelIndex)
					lChannelName = lChannel.GetName()
					lAnimCurve = lGeometry.GetShapeChannel(lBlendShapeIndex, lChannelIndex, pAnimLayer, True)
					if lAnimCurve:
						print("		Shape %s" % lChannelName)
						DisplayCurve(lAnimCurve)

	# Display curves specific to properties
	lProperty = pNode.GetFirstProperty()
	
	GoWhileLoop=lProperty.IsValid()
	print("lProperty.IsValid()==GoWhileLoop=="+str(GoWhileLoop))
	while GoWhileLoop:
		#print("GO While Loop")
		#"""
		if lProperty.GetFlag(FbxPropertyFlags.eUserDefined):
			lFbxFCurveNodeName  = lProperty.GetName()
			lCurveNode = lProperty.GetCurveNode(pAnimLayer)

			if not lCurveNode:
				lProperty = pNode.GetNextProperty(lProperty)
				continue

			lDataType = lProperty.GetPropertyDataType()
			if lDataType.GetType() == eFbxBool or lDataType.GetType() == eFbxDouble or lDataType.GetType() == eFbxFloat or lDataType.GetType() == eFbxInt:
				lMessage =  "		Property "
				lMessage += lProperty.GetName()
				if lProperty.GetLabel().GetLen() > 0:
					lMessage += " (Label: "
					lMessage += lProperty.GetLabel()
					lMessage += ")"

				DisplayString(lMessage)

				for c in range(lCurveNode.GetCurveCount(0)):
					lAnimCurve = lCurveNode.GetCurve(0, c)
					if lAnimCurve:
						DisplayCurve(lAnimCurve)
			elif lDataType.GetType() == eFbxDouble3 or lDataType.GetType() == eFbxDouble4 or lDataType.Is(FbxColor3DT) or lDataType.Is(FbxColor4DT):
				if lDataType.Is(FbxColor3DT) or lDataType.Is(FbxColor4DT):
					lComponentName1 = KFCURVENODE_COLOR_RED
					lComponentName2 = KFCURVENODE_COLOR_GREEN
					lComponentName3 = KFCURVENODE_COLOR_BLUE					
				else:
					lComponentName1 = "X"
					lComponentName2 = "Y"
					lComponentName3 = "Z"
				
				lMessage =  "		Property "
				lMessage += lProperty.GetName()
				if lProperty.GetLabel().GetLen() > 0:
					lMessage += " (Label: "
					lMessage += lProperty.GetLabel()
					lMessage += ")"
				DisplayString(lMessage)

				for c in range(lCurveNode.GetCurveCount(0)):
					lAnimCurve = lCurveNode.GetCurve(0, c)
					if lAnimCurve:
						DisplayString("		Component ", lComponentName1)
						DisplayCurve(lAnimCurve)

				for c in range(lCurveNode.GetCurveCount(1)):
					lAnimCurve = lCurveNode.GetCurve(1, c)
					if lAnimCurve:
						DisplayString("		Component ", lComponentName2)
						DisplayCurve(lAnimCurve)

				for c in range(lCurveNode.GetCurveCount(2)):
					lAnimCurve = lCurveNode.GetCurve(2, c)
					if lAnimCurve:
						DisplayString("		Component ", lComponentName3)
						DisplayCurve(lAnimCurve)
			elif lDataType.GetType() == eFbxEnum:
				lMessage =  "		Property "
				lMessage += lProperty.GetName()
				if lProperty.GetLabel().GetLen() > 0:
					lMessage += " (Label: "
					lMessage += lProperty.GetLabel()
					lMessage += ")"
				DisplayString(lMessage)

				for c in range(lCurveNode.GetCurveCount(0)):
					lAnimCurve = lCurveNode.GetCurve(0, c)
					if lAnimCurve:
						DisplayListCurve(lAnimCurve, lProperty)
	
		#"""	
		lProperty = pNode.GetNextProperty(lProperty)
		GoWhileLoop=lProperty.IsValid()
	#while Loop END Indent.
	
def InterpolationFlagToIndex(flags):
	#if (flags&KFCURVE_INTERPOLATION_CONSTANT)==KFCURVE_INTERPOLATION_CONSTANT:
	#	return 1
	#if (flags&KFCURVE_INTERPOLATION_LINEAR)==KFCURVE_INTERPOLATION_LINEAR:
	#	return 2
	#if (flags&KFCURVE_INTERPOLATION_CUBIC)==KFCURVE_INTERPOLATION_CUBIC:
	#	return 3
	return 0

def ConstantmodeFlagToIndex(flags):
	#if (flags&KFCURVE_CONSTANT_STANDARD)==KFCURVE_CONSTANT_STANDARD:
	#	return 1
	#if (flags&KFCURVE_CONSTANT_NEXT)==KFCURVE_CONSTANT_NEXT:
	#	return 2
	return 0

def TangeantmodeFlagToIndex(flags):
	#if (flags&KFCURVE_TANGEANT_AUTO) == KFCURVE_TANGEANT_AUTO:
	#	return 1
	#if (flags&KFCURVE_TANGEANT_AUTO_BREAK)==KFCURVE_TANGEANT_AUTO_BREAK:
	#	return 2
	#if (flags&KFCURVE_TANGEANT_TCB) == KFCURVE_TANGEANT_TCB:
	#	return 3
	#if (flags&KFCURVE_TANGEANT_USER) == KFCURVE_TANGEANT_USER:
	#	return 4
	#if (flags&KFCURVE_GENERIC_BREAK) == KFCURVE_GENERIC_BREAK:
	#	return 5
	#if (flags&KFCURVE_TANGEANT_BREAK) ==KFCURVE_TANGEANT_BREAK:
	#	return 6
	return 0

def TangeantweightFlagToIndex(flags):
	#if (flags&KFCURVE_WEIGHTED_NONE) == KFCURVE_WEIGHTED_NONE:
	#	return 1
	#if (flags&KFCURVE_WEIGHTED_RIGHT) == KFCURVE_WEIGHTED_RIGHT:
	#	return 2
	#if (flags&KFCURVE_WEIGHTED_NEXT_LEFT) == KFCURVE_WEIGHTED_NEXT_LEFT:
	#	return 3
	return 0

def TangeantVelocityFlagToIndex(flags):
	#if (flags&KFCURVE_VELOCITY_NONE) == KFCURVE_VELOCITY_NONE:
	#	return 1
	#if (flags&KFCURVE_VELOCITY_RIGHT) == KFCURVE_VELOCITY_RIGHT:
	#	return 2
	#if (flags&KFCURVE_VELOCITY_NEXT_LEFT) == KFCURVE_VELOCITY_NEXT_LEFT:
	#	return 3
	return 0

def DisplayCurveKeys(pCurve):
	interpolation = [ "?", "constant", "linear", "cubic"]
	constantMode =  [ "?", "Standard", "Next" ]
	cubicMode =	 [ "?", "Auto", "Auto break", "Tcb", "User", "Break", "User break" ]
	tangentWVMode = [ "?", "None", "Right", "Next left" ]

	lKeyCount = pCurve.KeyGetCount()

	for lCount in range(lKeyCount):
		lTimeString = ""
		lKeyValue = pCurve.KeyGetValue(lCount)
		lKeyTime  = pCurve.KeyGetTime(lCount)

		lOutputString = "			Key Time: "
		lOutputString += lKeyTime.GetTimeString(lTimeString)
		lOutputString += ".... Key Value: "
		lOutputString += str(lKeyValue)
		lOutputString += " [ "
		lOutputString += interpolation[ InterpolationFlagToIndex(pCurve.KeyGetInterpolation(lCount)) ]
		#if (pCurve.KeyGetInterpolation(lCount)&KFCURVE_INTERPOLATION_CONSTANT) == KFCURVE_INTERPOLATION_CONSTANT:
		#	lOutputString += " | "
		#	lOutputString += constantMode[ ConstantmodeFlagToIndex(pCurve.KeyGetConstantMode(lCount)) ]
		#elif (pCurve.KeyGetInterpolation(lCount)&KFCURVE_INTERPOLATION_CUBIC) == KFCURVE_INTERPOLATION_CUBIC:
		#	lOutputString += " | "
		#	lOutputString += cubicMode[ TangeantmodeFlagToIndex(pCurve.KeyGetTangeantMode(lCount)) ]
		#	lOutputString += " | "
		#	lOutputString += tangentWVMode[ TangeantweightFlagToIndex(pCurve.KeyGetTangeantWeightMode(lCount)) ]
		#	lOutputString += " | "
		#	lOutputString += tangentWVMode[ TangeantVelocityFlagToIndex(pCurve.KeyGetTangeantVelocityMode(lCount)) ]
			
		lOutputString += " ]"
		print(lOutputString)

def DisplayCurveDefault(pCurve):
	lOutputString = "			Default Value: "
	lOutputString += pCurve.GetValue()
	
	print(lOutputString)

def DisplayListCurveKeys(pCurve, pProperty):
	print ("===606=============DisplayListCurveKeys(pCurve"+str(pCurve)+", pProperty="+str(pProperty)+")=================")
	lKeyCount = pCurve.KeyGetCount()
	print ("===608=============lKeyCount="+str(lKeyCount)+"=================")
	
	for lCount in range(lKeyCount):
		lOutputString = "			Key Time: "
		lKeyValue = int(pCurve.KeyGetValue(lCount))
		lKeyTime  = pCurve.KeyGetTime(lCount)
		#lKeyTimeString
		#lKeyValue = static_cast<int>(pCurve.KeyGetValue(lCount))
		lOutputString = "			Key Time: "
		#lOutputString += str(lKeyTime.GetTimeString(lTimeString))
		lOutputString += str(lKeyTime)
		lOutputString += ".... Key Value: "
		lOutputString +=str( lKeyValue)
		lOutputString += " ("
		lOutputString += str(pProperty.GetEnumValue(lKeyValue))
		lOutputString += ")"

		print(lOutputString)
	
def DisplayListCurveDefault(pCurve, pProperty):
	DisplayCurveDefault(pCurve)

#===========================引用　D:\work\FBXSDK\FBX\FBX Python SDK\2016.1.1\samples\ImportScene\DisplayAnimation.py

#===================GetKeyCurve=========================	
class FBXData() :
	def DebugLog(strData):
		mystr=strData
		print(mystr)
	def FBXData(self):
		print ("==========================FBXData()=========================================")
		
	def loadFile(self, filename) :
		self.filename = filename
		self.root = None
		self.load()
	def load(self) :
		print ("loading ... self.filename= "+self.filename)
		#print "loading : %s"%self.filename
		manager = FbxManager.Create()
		ios = FbxIOSettings.Create(manager, IOSROOT)
		manager.SetIOSettings(ios)
		importer = FbxImporter.Create(manager, "")
		fbxImportSuccesBool=importer.Initialize(self.filename, -1, manager.GetIOSettings()) 
		print("fbxImportSuccesBool="+str(fbxImportSuccesBool))
		if not fbxImportSuccesBool:
			print ("==============Failed to load file.=============="+self.filename)
			return
		scene = FbxScene.Create(manager, "MyScene")
		importer.Import(scene)
		#importer.Initialize()
		
		fbxRoot = scene.GetRootNode()
		self.root = Node(fbxRoot.GetName(), None)
		getHierarchy(fbxRoot, self.root)
		#GetMesh(self.root)
		GetKeyCurve(importer,scene)
		
		
		print ("==============Succeeded to load file.========="+self.filename)
		
		
		print ("==============Destroy All=========")
		importer.Destroy()
		manager.Destroy()
		#//////////////////////////////////////////////////////////////////////////////////////////////////
		#//////////////////////////////////// Class Unit Test /////////////////////////////////////////////
		#//////////////////////////////////////////////////////////////////////////////////////////////////		
	def getClassName(self):
		DebugLog( u"className= " + self.__class__.__name__)
		return self.__class__.__name__

Instance = FBXData()  # Class  export  instance.
DebugLog(" FBXData Class  __name__="+__name__)
if(__name__ == Instance.getClassName()):
	DebugLog (u"__name__==self.__class__.__name__  Same!! File Test")
	DebugLog (u"=============Simple Single Class Unit Test Start==========")
	Instance.FBXData() #Call Method
	Instance.loadFile("Solder_Model_FBX_ASCII_2016_2017_settings_.fbx")
elif(__name__ == "fbxsdk00400class"):
	DebugLog (u"=============Simple Single Class Unit Test Start=====fbxsdk00300class=====")
	Instance.FBXData() #Call Method
	Instance.loadFile(FBX_FILE_PATH_AND_NAME_AND_EXT)
else:
	DebugLog (u"__name__!=self.__class__.__name__  Othor File Import")

	
	

