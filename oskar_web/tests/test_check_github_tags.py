# coding=utf-8
"""Tests of API access to GitHub."""


def test_get_github_tags():
    """Test getting a list of GitHub tags."""
    import github3
    import markdown2

    gh = github3.GitHub()
    repository = gh.repository(owner='OxfordSKA',
                               repository="OSKAR")

    latest_release = repository.latest_release()
    # print(markdown2.markdown(latest_release.body))
    releases = repository.releases()
    print()
    print('----------')
    print(latest_release.id, latest_release.name, latest_release.tarball_url)
    print('----------')
    for release in releases:
        print(release.id, release.name, release.tarball_url)


def test_get_github_releases():
    """Test getting a list of GitHub releases."""
