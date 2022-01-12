"""
* This file is part of PYSLAM 
*
* Copyright (C) 2016-present Luigi Freda <luigi dot freda at gmail dot com> 
*
* PYSLAM is free software: you can redistribute it and/or modify
* it under the terms of the GNU General Public License as published by
* the Free Software Foundation, either version 3 of the License, or
* (at your option) any later version.
*
* PYSLAM is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
* GNU General Public License for more details.
*
* You should have received a copy of the GNU General Public License
* along with PYSLAM. If not, see <http://www.gnu.org/licenses/>.
"""

from feature_tracker import feature_tracker_factory, FeatureTrackerTypes 
from feature_manager import feature_manager_factory
from feature_types import FeatureDetectorTypes, FeatureDescriptorTypes, FeatureInfo
from feature_matcher import feature_matcher_factory, FeatureMatcherTypes

from parameters import Parameters  


# some default parameters 

kNumFeatures=Parameters.kNumFeatures    

kRatioTest=Parameters.kFeatureMatchRatioTest

kTrackerType = FeatureTrackerTypes.DES_BF      # default descriptor-based, brute force matching with knn 
#kTrackerType = FeatureTrackerTypes.DES_FLANN  # default descriptor-based, FLANN-based matching 
        
        
"""
A collection of ready-to-used feature tracker configurations 
"""
class FeatureTrackerConfigs(object):   
    
    # Test/Template configuration: you can use this to quickly test 
    # - your custom parameters and 
    # - favourite descriptor and detector (check the file feature_types.py)
    TEST = dict(num_features=kNumFeatures,                   
                num_levels = 8,                                  # N.B: some detectors/descriptors do not allow to set num_levels or they set it on their own
                scale_factor = 1.2,                              # N.B: some detectors/descriptors do not allow to set scale_factor or they set it on their own
                detector_type = FeatureDetectorTypes.ORB2, 
                descriptor_type = FeatureDescriptorTypes.ORB2, 
                match_ratio_test = kRatioTest,
                tracker_type = kTrackerType)
    
    ######################################################
    #################### TEST CONFIG COMBINATION #########
    ######################################################
    # Format: T[XX]_[YY]_[ZZ];
    # XX is test ID number
    # YY is detector name
    # ZZ is descriptor name
    # there are 42 combinations + some deep learning


    test_configs = {         	 
        
        'T1_SIFT':dict(num_features=kNumFeatures,  
                        detector_type = FeatureDetectorTypes.SIFT, 
                        descriptor_type = FeatureDescriptorTypes.SIFT, 
                        match_ratio_test = kRatioTest,                         
                        tracker_type = kTrackerType), # done

        'T2_SURF':dict(num_features=kNumFeatures,
                        num_levels = 8,
                        detector_type = FeatureDetectorTypes.SURF, 
                        descriptor_type = FeatureDescriptorTypes.SURF, 
                        match_ratio_test = kRatioTest,                         
                        tracker_type = kTrackerType), # done

        'T3_BRISK':dict(num_features=kNumFeatures,  
                        num_levels = 4, 
                        scale_factor = 1.2,
                        detector_type = FeatureDetectorTypes.BRISK,
                        descriptor_type = FeatureDescriptorTypes.BRISK,
                        match_ratio_test = kRatioTest,                           
                        tracker_type = kTrackerType), # done
                                       
        'T4_FAST':dict(num_features=kNumFeatures,  
                        num_levels = 8, 
                        scale_factor = 1.2,
                        detector_type = FeatureDetectorTypes.FAST, 
                        descriptor_type = FeatureDescriptorTypes.NONE, 
                        tracker_type = FeatureTrackerTypes.LK), # done
                        
        'T5_ORB':dict(num_features=kNumFeatures, 
                       num_levels = 8, 
                       scale_factor = 1.2, 
                       detector_type = FeatureDetectorTypes.ORB, 
                       descriptor_type = FeatureDescriptorTypes.ORB, 
                       match_ratio_test = kRatioTest,                        
                       tracker_type = kTrackerType),

        }

