import zig

# data = [
#     [
#         '      ',
#         ' A  A ',
#         '      ',
#         '      ',
#         ' A  B ',
#         '      '],
#     [1, 1, 0, 3, 4, 4, 2, 5, 1, 4]]
#
# answer = [None, [5, 4], [0, 5], [3, 5], [0, 4], [5, 1], [2, 5], [5, 5], None, [5, 1]]

data = [
    [
        ' A    A ',
        '  A  B  ',
        '    B   ',
        '   B    ',
        '    A A ',
        '  B  A  ',
        '   A    ',
        ' B    B '],
    [0, 1, 2, 3, 4, 5, 6, 7, 3, 6, 3, 1, 2, 6, 1]]

answer = [None, None, [0, 4], [0, 3], [7, 4], [7, 2], [7, 3], [7, 1], None, [7, 3], [0, 3], [0, 2], None, None, None]

artifact = data[0]
explorers = data[1]

# switches_outside, height_outside, width_outside = parse_artifact(artifact_outside)
# for switch_outside in switches_outside:
#     print(switch_outside)

print(zig.ride_of_fortune(artifact, explorers))
