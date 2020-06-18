import logging
from tests.helpers import *
import loopy_turtles

class Tests:

  def test_draw_square_turning_left(self, monkeypatch):
    """
    Test that the square is drawn correctly by the turtle.
    """
    # set up debug logging
    # log = logging.getLogger('test_get_square_turning_left')

    t = loopy_turtles.create_turtle('red', 'yellow') # create a turtle object

    # get some clean data for each function's data
    mock_functions = {}
    mock_data = {}

    # handle loopy_turtles functions, which are not within an object
    mock_functions['loopy_turtles.pick_up_and_move_turtle'] = get_mock_function(mock_data, 'loopy_turtles.pick_up_and_move_turtle')
    monkeypatch.setattr('loopy_turtles.pick_up_and_move_turtle', lambda *args: mock_functions['loopy_turtles.pick_up_and_move_turtle']('loopy_turtles.pick_up_and_move_turtle', args))

    mock_functions['loopy_turtles.print_turtle_position'] = get_mock_function(mock_data, 'loopy_turtles.print_turtle_position')
    monkeypatch.setattr('loopy_turtles.print_turtle_position', lambda *args: mock_functions['loopy_turtles.print_turtle_position']('loopy_turtles.print_turtle_position', args))

    # mock the print_turtle_position functions
    mock_functions['t.forward'] = get_mock_function(mock_data, 't.forward')
    monkeypatch.setattr(t, 'forward', lambda *args: mock_functions['t.forward']('t.forward', args))
    monkeypatch.setattr(t, 'fd', lambda *args: mock_functions['t.forward']('t.forward', args))

    mock_functions['t.right'] = get_mock_function(mock_data, 't.right')
    monkeypatch.setattr(t, 'right', lambda *args: mock_functions['t.right']('t.right', args))

    mock_functions['t.left'] = get_mock_function(mock_data, 't.left')
    monkeypatch.setattr(t, 'left', lambda *args: mock_functions['t.left']('t.left', args))

    mock_functions['t.fillcolor'] = get_mock_function(mock_data, 't.fillcolor')
    monkeypatch.setattr(t, 'fillcolor', lambda *args: mock_functions['t.fillcolor']('t.fillcolor', args))

    mock_functions['t.begin_fill'] = get_mock_function(mock_data, 't.begin_fill')
    monkeypatch.setattr(t, 'begin_fill', lambda *args: mock_functions['t.begin_fill']('t.begin_fill', args))

    mock_functions['t.end_fill'] = get_mock_function(mock_data, 't.end_fill')
    monkeypatch.setattr(t, 'end_fill', lambda *args: mock_functions['t.end_fill']('t.end_fill', args))

    # call the function in question
    x = 10
    y = 10
    length = 200
    direction = 'left'
    loopy_turtles.draw_square(t, x, y, length, direction, 'red')

    # assert truths
    assert mock_data['loopy_turtles.pick_up_and_move_turtle']['call_counter'] == 1
    assert mock_data['loopy_turtles.pick_up_and_move_turtle']['params']['actual'][1] == x
    assert mock_data['loopy_turtles.pick_up_and_move_turtle']['params']['actual'][2] == y

    assert mock_data['loopy_turtles.print_turtle_position']['call_counter'] == 4

    assert mock_data['t.forward']['call_counter'] == 4
    assert mock_data['t.forward']['params']['actual'] == [length, length, length, length]

    assert mock_data['t.right']['call_counter'] == 0

    assert mock_data['t.left']['call_counter'] == 4
    assert mock_data['t.left']['params']['actual'] == [90, 90, 90, 90]

    assert mock_data['t.begin_fill']['call_counter'] == 1
    assert mock_data['t.end_fill']['call_counter'] == 1

  def test_draw_square_turning_right(self, monkeypatch):
    """
    Test that the square is drawn correctly by the turtle.
    """
    # set up debug logging
    # log = logging.getLogger('test_get_square_turning_right')

    t = loopy_turtles.create_turtle('red', 'yellow') # create a turtle object

    # get some clean data for each function's data
    mock_functions = {}
    mock_data = {}

    # handle loopy_turtles functions, which are not within an object
    mock_functions['loopy_turtles.pick_up_and_move_turtle'] = get_mock_function(mock_data, 'loopy_turtles.pick_up_and_move_turtle')
    monkeypatch.setattr('loopy_turtles.pick_up_and_move_turtle', lambda *args: mock_functions['loopy_turtles.pick_up_and_move_turtle']('loopy_turtles.pick_up_and_move_turtle', args))

    mock_functions['loopy_turtles.print_turtle_position'] = get_mock_function(mock_data, 'loopy_turtles.print_turtle_position')
    monkeypatch.setattr('loopy_turtles.print_turtle_position', lambda *args: mock_functions['loopy_turtles.print_turtle_position']('loopy_turtles.print_turtle_position', args))

    # mock the print_turtle_position functions
    mock_functions['t.forward'] = get_mock_function(mock_data, 't.forward')
    monkeypatch.setattr(t, 'forward', lambda *args: mock_functions['t.forward']('t.forward', args))
    monkeypatch.setattr(t, 'fd', lambda *args: mock_functions['t.forward']('t.forward', args))

    mock_functions['t.right'] = get_mock_function(mock_data, 't.right')
    monkeypatch.setattr(t, 'right', lambda *args: mock_functions['t.right']('t.right', args))

    mock_functions['t.left'] = get_mock_function(mock_data, 't.left')
    monkeypatch.setattr(t, 'left', lambda *args: mock_functions['t.left']('t.left', args))

    mock_functions['t.fillcolor'] = get_mock_function(mock_data, 't.fillcolor')
    monkeypatch.setattr(t, 'fillcolor', lambda *args: mock_functions['t.fillcolor']('t.fillcolor', args))

    mock_functions['t.begin_fill'] = get_mock_function(mock_data, 't.begin_fill')
    monkeypatch.setattr(t, 'begin_fill', lambda *args: mock_functions['t.begin_fill']('t.begin_fill', args))

    mock_functions['t.end_fill'] = get_mock_function(mock_data, 't.end_fill')
    monkeypatch.setattr(t, 'end_fill', lambda *args: mock_functions['t.end_fill']('t.end_fill', args))

    # call the function in question
    x = 200
    y = 200
    length = 100
    direction = 'right'
    loopy_turtles.draw_square(t, x, y, length, direction, 'red')

    # assert truths
    assert mock_data['loopy_turtles.pick_up_and_move_turtle']['call_counter'] == 1
    assert mock_data['loopy_turtles.pick_up_and_move_turtle']['params']['actual'][1] == x
    assert mock_data['loopy_turtles.pick_up_and_move_turtle']['params']['actual'][2] == y

    assert mock_data['loopy_turtles.print_turtle_position']['call_counter'] == 4

    assert mock_data['t.forward']['call_counter'] == 4
    assert mock_data['t.forward']['params']['actual'] == [length, length, length, length]

    assert mock_data['t.left']['call_counter'] == 0

    assert mock_data['t.right']['call_counter'] == 4
    assert mock_data['t.right']['params']['actual'] == [90, 90, 90, 90]

    assert mock_data['t.begin_fill']['call_counter'] == 1
    assert mock_data['t.end_fill']['call_counter'] == 1

  def test_draw_pentagon_turning_left(self, monkeypatch):
    """
    Test that the pentagon is drawn correctly by the turtle, first turning left
    """
    # set up debug logging
    # log = logging.getLogger('test_draw_pentagon_turning_left')

    t = loopy_turtles.create_turtle('red', 'yellow') # create a turtle object

    # get some clean data for each function's data
    mock_functions = {}
    mock_data = {}

    # handle loopy_turtles functions, which are not within an object
    mock_functions['loopy_turtles.pick_up_and_move_turtle'] = get_mock_function(mock_data, 'loopy_turtles.pick_up_and_move_turtle')
    monkeypatch.setattr('loopy_turtles.pick_up_and_move_turtle', lambda *args: mock_functions['loopy_turtles.pick_up_and_move_turtle']('loopy_turtles.pick_up_and_move_turtle', args))

    mock_functions['loopy_turtles.print_turtle_position'] = get_mock_function(mock_data, 'loopy_turtles.print_turtle_position')
    monkeypatch.setattr('loopy_turtles.print_turtle_position', lambda *args: mock_functions['loopy_turtles.print_turtle_position']('loopy_turtles.print_turtle_position', args))

    # mock the print_turtle_position functions
    mock_functions['t.forward'] = get_mock_function(mock_data, 't.forward')
    monkeypatch.setattr(t, 'forward', lambda *args: mock_functions['t.forward']('t.forward', args))
    monkeypatch.setattr(t, 'fd', lambda *args: mock_functions['t.forward']('t.forward', args))

    mock_functions['t.right'] = get_mock_function(mock_data, 't.right')
    monkeypatch.setattr(t, 'right', lambda *args: mock_functions['t.right']('t.right', args))

    mock_functions['t.left'] = get_mock_function(mock_data, 't.left')
    monkeypatch.setattr(t, 'left', lambda *args: mock_functions['t.left']('t.left', args))

    mock_functions['t.fillcolor'] = get_mock_function(mock_data, 't.fillcolor')
    monkeypatch.setattr(t, 'fillcolor', lambda *args: mock_functions['t.fillcolor']('t.fillcolor', args))

    mock_functions['t.begin_fill'] = get_mock_function(mock_data, 't.begin_fill')
    monkeypatch.setattr(t, 'begin_fill', lambda *args: mock_functions['t.begin_fill']('t.begin_fill', args))

    mock_functions['t.end_fill'] = get_mock_function(mock_data, 't.end_fill')
    monkeypatch.setattr(t, 'end_fill', lambda *args: mock_functions['t.end_fill']('t.end_fill', args))

    # call the function in question
    x = 200
    y = 200
    length = 50
    direction = 'left'
    angle = 90
    loopy_turtles.draw_pentagon(t, x, y, length, angle, direction, 'red') # draw a pentagon

    # assert truths
    assert mock_data['loopy_turtles.pick_up_and_move_turtle']['call_counter'] == 1
    assert mock_data['loopy_turtles.pick_up_and_move_turtle']['params']['actual'][1] == x
    assert mock_data['loopy_turtles.pick_up_and_move_turtle']['params']['actual'][2] == y

    assert mock_data['loopy_turtles.print_turtle_position']['call_counter'] == 5

    assert mock_data['t.forward']['call_counter'] == 10
    assert mock_data['t.forward']['params']['actual'] == [length, length, length, length, length, length, length, length, length, length]

    assert mock_data['t.left']['call_counter'] == 5
    assert mock_data['t.left']['params']['actual'] == [90, 90, 90, 90, 90]

    assert mock_data['t.right']['call_counter'] == 5
    assert mock_data['t.right']['params']['actual'] == [18, 18, 18, 18, 18]

    assert mock_data['t.begin_fill']['call_counter'] == 1
    assert mock_data['t.end_fill']['call_counter'] == 1

  def test_draw_pentagon_turning_right(self, monkeypatch):
    """
    Test that the square is drawn correctly by the turtle.
    """
    # set up debug logging
    # log = logging.getLogger('test_draw_pentagon_turning_left')

    t = loopy_turtles.create_turtle('red', 'yellow') # create a turtle object

    # get some clean data for each function's data
    mock_functions = {}
    mock_data = {}

    # handle loopy_turtles functions, which are not within an object
    mock_functions['loopy_turtles.pick_up_and_move_turtle'] = get_mock_function(mock_data, 'loopy_turtles.pick_up_and_move_turtle')
    monkeypatch.setattr('loopy_turtles.pick_up_and_move_turtle', lambda *args: mock_functions['loopy_turtles.pick_up_and_move_turtle']('loopy_turtles.pick_up_and_move_turtle', args))

    mock_functions['loopy_turtles.print_turtle_position'] = get_mock_function(mock_data, 'loopy_turtles.print_turtle_position')
    monkeypatch.setattr('loopy_turtles.print_turtle_position', lambda *args: mock_functions['loopy_turtles.print_turtle_position']('loopy_turtles.print_turtle_position', args))

    # mock the print_turtle_position functions
    mock_functions['t.forward'] = get_mock_function(mock_data, 't.forward')
    monkeypatch.setattr(t, 'forward', lambda *args: mock_functions['t.forward']('t.forward', args))
    monkeypatch.setattr(t, 'fd', lambda *args: mock_functions['t.forward']('t.forward', args))

    mock_functions['t.right'] = get_mock_function(mock_data, 't.right')
    monkeypatch.setattr(t, 'right', lambda *args: mock_functions['t.right']('t.right', args))

    mock_functions['t.left'] = get_mock_function(mock_data, 't.left')
    monkeypatch.setattr(t, 'left', lambda *args: mock_functions['t.left']('t.left', args))

    mock_functions['t.fillcolor'] = get_mock_function(mock_data, 't.fillcolor')
    monkeypatch.setattr(t, 'fillcolor', lambda *args: mock_functions['t.fillcolor']('t.fillcolor', args))

    mock_functions['t.begin_fill'] = get_mock_function(mock_data, 't.begin_fill')
    monkeypatch.setattr(t, 'begin_fill', lambda *args: mock_functions['t.begin_fill']('t.begin_fill', args))

    mock_functions['t.end_fill'] = get_mock_function(mock_data, 't.end_fill')
    monkeypatch.setattr(t, 'end_fill', lambda *args: mock_functions['t.end_fill']('t.end_fill', args))

    # call the function in question
    x = 10
    y = 10
    length = 200
    direction = 'right'
    angle = 120
    loopy_turtles.draw_pentagon(t, x, y, length, angle, direction, 'red') # draw a pentagon

    # assert truths
    assert mock_data['loopy_turtles.pick_up_and_move_turtle']['call_counter'] == 1
    assert mock_data['loopy_turtles.pick_up_and_move_turtle']['params']['actual'][1] == x
    assert mock_data['loopy_turtles.pick_up_and_move_turtle']['params']['actual'][2] == y

    assert mock_data['loopy_turtles.print_turtle_position']['call_counter'] == 5

    assert mock_data['t.forward']['call_counter'] == 10
    assert mock_data['t.forward']['params']['actual'] == [length, length, length, length, length, length, length, length, length, length]

    assert mock_data['t.right']['call_counter'] == 5
    assert mock_data['t.right']['params']['actual'] == [120, 120, 120, 120, 120]

    assert mock_data['t.left']['call_counter'] == 5
    assert mock_data['t.left']['params']['actual'] == [48, 48, 48, 48, 48]

    assert mock_data['t.begin_fill']['call_counter'] == 1
    assert mock_data['t.end_fill']['call_counter'] == 1
