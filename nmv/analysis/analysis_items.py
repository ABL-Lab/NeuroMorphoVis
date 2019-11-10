####################################################################################################
# Copyright (c) 2016 - 2019, EPFL / Blue Brain Project
#               Marwan Abdellah <marwan.abdellah@epfl.ch>
#
# This file is part of NeuroMorphoVis <https://github.com/BlueBrain/NeuroMorphoVis>
#
# This program is free software: you can redistribute it and/or modify it under the terms of the
# GNU General Public License as published by the Free Software Foundation, version 3 of the License.
#
# This Blender-based tool is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
# PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.
####################################################################################################

# Internal imports
from nmv.analysis.structs import AnalysisItem
from nmv.analysis.kernels.morphology import *


####################################################################################################
# A list of all the analysis items (kernels) that will applied on the morphology skeleton per arbor
####################################################################################################
ui_per_arbor_analysis_items = [

    ################################################################################################
    # Samples-related items
    ################################################################################################
    AnalysisItem(variable='TotalNumberSamples',
                 name='Total # Samples',
                 kernel=kernel_total_number_samples,
                 description='The total number of samples',
                 data_format='INT'),

    AnalysisItem(variable='TotalNumberSections',
                 name='Total # Sections',
                 kernel=kernel_total_number_sections,
                 description='The total number of sections (or branches)',
                 data_format='INT'),

    AnalysisItem(variable='MaximumBranchingOrder',
                 name='Max. Branching Order',
                 kernel=kernel_maximum_branching_order,
                 description='The maximum branching order',
                 data_format='INT'),

    AnalysisItem(variable='TotalNumberBifurcations',
                 name='Total # Bifurcations',
                 kernel=kernel_total_number_bifurcations,
                 description='The total number of bifurcations',
                 data_format='INT'),

    AnalysisItem(variable='TotalNumberTrifurcations',
                 name='Total # Trifurcations',
                 kernel=kernel_total_number_trifurcations,
                 description='The total number of trifurcations',
                 data_format='INT'),

    AnalysisItem(variable='MaximumPathDistance',
                 name='Max. Path Distance',
                 kernel=kernel_maximum_path_distance,
                 description='The maximum distance along an arbor from its root sample to its '
                             'most far leaf',
                 data_format='FLOAT'),

    AnalysisItem(variable='MinNumberSamplePerSection',
                 name='Min. # Samples / Section',
                 kernel=kernel_minimum_number_samples_per_section,
                 description='The least number of samples per section',
                 data_format='INT'),

    AnalysisItem(variable='MaxNumberSamplePerSection',
                 name='Max. # Samples / Section',
                 kernel=kernel_maximum_number_samples_per_section,
                 description='The largest number of samples per section',
                 data_format='INT'),

    AnalysisItem(variable='AvgNumberSamplePerSection',
                 name='Avg. # Samples / Section',
                 kernel=kernel_average_number_samples_per_section,
                 description='The Average number of samples per  section',
                 data_format='INT'),

    AnalysisItem(variable='MinSampleRadius',
                 name='Min. Sample Radius',
                 kernel=kernel_minimum_sample_radius,
                 description='The minimum sample radius',
                 data_format='FLOAT'),

    AnalysisItem(variable='MaxSampleRadius',
                 name='Max. Sample Radius',
                 kernel=kernel_maximum_sample_radius,
                 description='The maximum sample radius',
                 data_format='FLOAT'),

    AnalysisItem(variable='AvgSampleRadius',
                 name='Avg. Sample Radius',
                 kernel=kernel_average_sample_radius,
                 description='The average sample radius',
                 data_format='FLOAT'),

    AnalysisItem(variable='ZeroRadiiSamples',
                 name='Zero-radius Samples',
                 kernel=kernel_number_zero_radius_samples,
                 description='The total number of zero-radius samples',
                 data_format='INT'),

    ################################################################################################
    # Length-related items
    ################################################################################################
    AnalysisItem(variable='TotalLength',
                 name='Total Length',
                 kernel=kernel_total_length,
                 description='Total length',
                 data_format='FLOAT',
                 unit='LENGTH'),

    AnalysisItem(variable='MinSectionLength',
                 name='Min. Section Length',
                 kernel=kernel_minimum_section_length,
                 description='The maximum section length',
                 data_format='FLOAT',
                 unit='LENGTH'),

    AnalysisItem(variable='MaxSectionLength',
                 name='Max. Section Length',
                 kernel=kernel_maximum_section_length,
                 description='The minimum section length',
                 data_format='FLOAT',
                 unit='LENGTH'),

    AnalysisItem(variable='AvgSectionLength',
                 name='Avg. Section Length',
                 kernel=kernel_average_section_length,
                 description='Average section length',
                 data_format='FLOAT',
                 unit='LENGTH'),

    AnalysisItem(variable='ShortSections',
                 name='Short Sections',
                 kernel=kernel_short_sections,
                 description='The total number of short sections '
                             '(length is smaller than the sum of the terminal samples radii)',
                 data_format='INT'),

    AnalysisItem(variable='MinSegmentLength',
                 name='Min. Segment Length ',
                 kernel=kernel_minimum_segment_length,
                 description='The minimum segment length',
                 data_format='FLOAT',
                 unit='LENGTH'),

    AnalysisItem(variable='MaxSegmentLength',
                 name='Max. Segment Length ',
                 kernel=kernel_maximum_segment_length,

                 description='The maximum segment length',
                 data_format='FLOAT',
                 unit='LENGTH'),

    AnalysisItem(variable='AvgSegmentLength',
                 name='Avg. Segment Length ',
                 kernel=kernel_average_segment_length,
                 description='The average segment length',
                 data_format='FLOAT',
                 unit='LENGTH'),

    AnalysisItem(variable='ZeroLengthSegments',
                 name='Zero-length Segments',
                 kernel=kernel_zero_length_segments,
                 description='The total number of zero-length segments (or duplicate samples)',
                 data_format='INT'),

    ################################################################################################
    # Area-related items
    ################################################################################################
    AnalysisItem(variable='TotalSurfaceArea',
                 name='Total Surface Area',
                 kernel=kernel_total_surface_area,
                 description='Total surface area',
                 data_format='FLOAT',
                 unit='AREA'),

    AnalysisItem(variable='MinSectionSurfaceArea',
                 name='Min. Section Surface Area',
                 kernel=kernel_minimum_section_surface_area,
                 description='The minimum section surface area',
                 data_format='FLOAT',
                 unit='AREA'),

    AnalysisItem(variable='MaxSectionSurfaceArea',
                 name='Max. Section Surface Area',
                 kernel=kernel_maximum_section_surface_area,
                 description='The maximum section surface area',
                 data_format='FLOAT',
                 unit='AREA'),

    AnalysisItem(variable='AvgSurfaceAreaPerSection',
                 name='Avg. Section Surface Area',
                 kernel=kernel_average_section_surface_area,
                 description='The average section surface area',
                 data_format='FLOAT',
                 unit='AREA'),

    ################################################################################################
    # Volume-related items
    ################################################################################################
    AnalysisItem(variable='TotalVolume',
                 name='Total Volume',
                 kernel=kernel_total_volume,
                 description='the total volume',
                 data_format='FLOAT',
                 unit='VOLUME'),

    AnalysisItem(variable='MinSectionVolume',
                 name='Min. Section Volume',
                 kernel=kernel_minimum_section_volume,
                 description='The minimum section volume',
                 data_format='FLOAT',
                 unit='VOLUME'),

    AnalysisItem(variable='MaxSectionVolume',
                 name='Max. Section Volume',
                 kernel=kernel_maximum_section_volume,
                 description='The maximum section volume',
                 data_format='FLOAT',
                 unit='VOLUME'),

    AnalysisItem(variable='AvgSectionVolume',
                 name='Avg. Section Volume',
                 kernel=kernel_average_section_volume,
                 description='The average section volume',
                 data_format='FLOAT',
                 unit='VOLUME'),
]


####################################################################################################
# Global analysis items, only applied on a global level not per-arbor level
####################################################################################################
ui_global_analysis_items = [

    ################################################################################################
    # Soma items
    ################################################################################################
    AnalysisItem(variable='SomaReportedRadius',
                 name='Soma Reported Radius',
                 kernel=kernel_soma_get_reported_mean_radius,
                 description='The radius of the soma as reported in the morphology file',
                 data_format='FLOAT'),

    AnalysisItem(variable='SomaMinimumRadius',
                 name='Soma Min. Radius',
                 kernel=kernel_soma_get_minimum_radius,
                 description='The minimum radius of the soma as based on the reported profile '
                             'points and the root samples of all the connected arbors (or stems)',
                 data_format='FLOAT'),

    AnalysisItem(variable='SomaMaximumRadius',
                 name='Soma Max. Radius',
                 kernel=kernel_soma_get_maximum_radius,
                 description='The maximum radius of the soma as based on the reported profile '
                             'points and the root samples of all the connected arbors (or stems)',
                 data_format='FLOAT'),

    AnalysisItem(variable='ReportedSomaSurfaceArea',
                 name='Soma Surface Area',
                 kernel=kernel_soma_get_average_surface_area,
                 description='The surface area of the soma as reported in the morphology file '
                             'in mμ²',
                 data_format='FLOAT'),

    AnalysisItem(variable='ReportedSomaVolume',
                 name='Soma Volume',
                 kernel=kernel_soma_get_average_volume,
                 description='The volume of the soma as reported in the morphology file in mμ³',
                 data_format='FLOAT'),

    AnalysisItem(variable='NumberProfilePoints',
                 name='# Profile Points',
                 kernel=kernel_soma_count_profile_points,
                 description='The radius of the soma as reported in the morphology file',
                 data_format='INT'),

    ################################################################################################
    # Arborization items
    ################################################################################################
    AnalysisItem(variable='NumberApicalDendrites',
                 name='Apical Dendrites',
                 kernel=kernel_global_number_apical_dendrites,
                 description='The total number of apical dendrites in the morphology',
                 data_format='INT'),

    AnalysisItem(variable='NumberBasalDendrites',
                 name='Basal Dendrites',
                 kernel=kernel_global_number_basal_dendrites,
                 description='The total number of basal dendrites in the morphology',
                 data_format='INT'),

    AnalysisItem(variable='NumberAxons',
                 name='Axons',
                 kernel=kernel_global_number_axons,
                 description='The total number of axons in the morphology',
                 data_format='INT'),

    AnalysisItem(variable='NumberNeurites',
                 name='Total # Neurites',
                 kernel=kernel_global_total_number_neurites,
                 description='The total number of the arbors in the morphology '
                             'whether connected to the soma or not',
                 data_format='INT'),

    AnalysisItem(variable='NumberStems',
                 name='Total # Stems',
                 kernel=kernel_global_total_number_stems,
                 description='The total number of stems or the arbors that emanate from the '
                             'soma in the morphology',
                 data_format='INT'),
]
